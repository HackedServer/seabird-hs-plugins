import boto3
import requests
import re
import os

from typing import Tuple, Any

import seabird_pb2


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
        Image={"Bytes": imagedata,}, MaxLabels=5, MinConfidence=70,
    )

    message = []

    for i in response["Labels"]:
        message.append(f'{i["Name"]} ({round(i["Confidence"],0)}%)')

    return True, ", ".join(message)


def submit_to_rekognition_celebrity(
    imagedata
) -> Tuple[bool, str]:

    client = boto3.client(
        "rekognition",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    )

    response = client.recognize_celebrities(Image={"Bytes": imagedata,},)

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
        return True, r.content
    else:
        return False, "Error message one day"
