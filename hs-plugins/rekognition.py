import boto3
import requests
import re
import os
import io

from PIL import Image
from typing import Tuple, Any


def analyze_url(stub, url: str):

    r = requests.head(url, allow_redirects=True, timeout=1)
    if re.search(
        "image/(jpeg|png)", r.headers["Content-Type"], flags=re.IGNORECASE
    ):
        return analyze_image(stub, url)


def analyze_image(stub, imageurl: str):

    ok, result = download_image(imageurl)
    if ok is not True:
        return ok, result
    ok, result = submit_to_rekognition(result)

    return result


def analyze_celebrity(stub, imageurl: str):

    ok, result = download_image(imageurl)
    if ok is not True:
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
        Image={"Bytes": imagedata}, MaxLabels=5, MinConfidence=70,
    )

    message = []

    for i in response["Labels"]:
        message.append(f'{i["Name"]} ({round(i["Confidence"],0)}%)')

    return True, ", ".join(message)


def submit_to_rekognition_celebrity(imagedata) -> Tuple[bool, str]:

    client = boto3.client(
        "rekognition",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    )

    response = client.recognize_celebrities(Image={"Bytes": imagedata},)

    message = ""

    print(response)
    for i in response["CelebrityFaces"]:
        message += f'{i["Name"]}, '

    print(message)

    return True, message


def download_image(imageurl: str) -> Tuple[bool, Any]:
    """Downloads the image url and returns a success/fail bool, message or image data"""

    r = requests.get(imageurl, stream=True, timeout=1)

    if r.status_code == requests.codes.ok:
        r.raw.decode_content = True
        print(f"{len(r.content)} Bytes")
        return True, r.content
    else:
        return False, "Error message one day"


def limit_img_size(
    img_filename, img_target_filename, target_filesize, tolerance=5
):
    img = img_orig = Image.open(img_filename)
    aspect = img.size[0] / img.size[1]

    while True:
        with io.BytesIO() as buffer:
            img.save(buffer, format="JPEG")
            data = buffer.getvalue()
        filesize = len(data)
        size_deviation = filesize / target_filesize
        print("size: {}; factor: {:.3f}".format(filesize, size_deviation))

        if size_deviation <= (100 + tolerance) / 100:
            # filesize fits
            with open(img_target_filename, "wb") as f:
                f.write(data)
            break
        else:
            # filesize not good enough => adapt width and height
            # use sqrt of deviation since applied both in width and height
            new_width = img.size[0] / size_deviation ** 0.5
            new_height = new_width / aspect
            # resize from img_orig to not lose quality
            img = img_orig.resize((int(new_width), int(new_height)))
