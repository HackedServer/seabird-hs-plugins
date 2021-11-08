import boto3
import requests
import re
import os
import io
import logging

from PIL import Image
from typing import Tuple, Any

LOG = logging.getLogger("hs-plugins")


def check_header(url: str) -> bool:

    try:
        r = requests.head(url, allow_redirects=True, timeout=1)
    except requests.exceptions.MissingSchema:
        try:
            r = requests.head(f"https://{url}", allow_redirects=True, timeout=1)
        except:
            LOG.error("Error https fetching %s", url)
            return False
    except:
        LOG.error("Error fetching %s", url)
        return False

    if re.search("image/(jpeg|png)", r.headers["Content-Type"], flags=re.IGNORECASE):
        LOG.info("Image content detected for: %s", url)
        return True
    else:
        LOG.info("Image content not detected for: %s", url)
        return False


def analyze_url(stub, url: str):

    if not check_header(url):
        return

    ok, result = download_image(url)
    if ok is not True:
        LOG.info("Failed to download image for: %s", url)
        return

    ok, result = submit_to_rekognition(result)

    if ok is True:
        return result


def analyze_image(imageurl: str):

    if not check_header(imageurl):
        return "No image detected."

    ok, result = download_image(imageurl)
    if ok is not True:
        LOG.info("Failed to download image for: %s", imageurl)
        return ok, result
    ok, result = submit_to_rekognition(result)

    return result


def analyze_celebrity(imageurl: str):

    if not check_header(imageurl):
        return "Image not detected."
    ok, result = download_image(imageurl)
    if ok is not True:
        LOG.info("Failed to download image for: %s", imageurl)
        return ok, result
    ok, result = submit_to_rekognition_celebrity(result)
    return result


def submit_to_rekognition(imagedata) -> Tuple[bool, str]:

    client = boto3.client(
        "rekognition",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    )

    response = client.detect_labels(
        Image={"Bytes": imagedata},
        MaxLabels=5,
        MinConfidence=70,
    )

    message = []

    for i in response["Labels"]:
        message.append(f'{i["Name"]} ({round(i["Confidence"])}%)')

    return True, ", ".join(message)


def submit_to_rekognition_celebrity(imagedata) -> Tuple[bool, str]:

    client = boto3.client(
        "rekognition",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    )

    response = client.recognize_celebrities(
        Image={"Bytes": imagedata},
    )

    message = ""

    print(response)
    for i in response["CelebrityFaces"]:
        message += f'{i["Name"]}, '

    print(message)

    return True, message


def download_image(imageurl: str) -> Tuple[bool, Any]:
    """Downloads the image url and returns a success/fail bool and message or image data"""

    try:
        r = requests.get(imageurl, stream=True, timeout=2)
    except requests.exceptions.MissingSchema:
        try:
            r = requests.get(f"https://{imageurl}", stream=True, timeout=2)
        except:
            pass

    if r.status_code == requests.codes.ok:
        r.raw.decode_content = True
        if len(r.content) > 5_000_000:
            shrunk_image = limit_image_size(r.content)
            return True, shrunk_image
        else:
            return True, r.content
    else:
        return False, "Error message one day"


def limit_image_size(original_image: bytes, target_filesize: int = 5_000_000) -> bytes:
    img = Image.open(io.BytesIO(original_image))
    aspect = img.size[0] / img.size[1]

    if img.size[0] > 1920:
        img = img.resize((1920, int(1920 / aspect)))

    if img.size[1] > 1080:
        img = img.resize((int(aspect * 1080), 1080))

    for _ in range(1, 5):
        with io.BytesIO() as buffer:
            img.save(buffer, format="JPEG", optimize=True)
            data = buffer.getvalue()
        filesize = len(data)
        size_deviation = filesize / target_filesize
        if size_deviation <= 1:
            return data
        else:
            new_width = img.size[0] / size_deviation ** 0.5
            new_height = new_width / aspect
            img = img.resize((int(new_width), int(new_height)))
