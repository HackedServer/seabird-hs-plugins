import boto3
import requests
import re

from configparser import ConfigParser
from typing import Tuple, Any

import seabird_pb2


def analyze_url(stub, config: ConfigParser, url: str):

    r = requests.head(url, allow_redirects=True, timeout=1)
    if re.search(
        "image/(jpeg|png)", r.headers["Content-Type"], flags=re.IGNORECASE
    ):
        return analyze_image(stub, config, url)


def analyze_image(stub, config: ConfigParser, imageurl: str):

    ok, result = download_image(imageurl)
    if ok is not True:
        return ok, result
    ok, result = submit_to_rekognition(config, result)

    return result


def analyze_celebrity(stub, config: ConfigParser, imageurl: str):

    ok, result = download_image(imageurl)
    if ok is not True:
        return ok, result
    ok, result = submit_to_rekognition_celebrity(config, result)

    return result


def submit_to_rekognition(config: ConfigParser, imagedata) -> Tuple[bool, str]:

    client = boto3.client(
        "rekognition",
        region_name=config["aws"]["region"],
        aws_access_key_id=config["aws"]["access_key"],
        aws_secret_access_key=config["aws"]["secret_key"],
    )

    response = client.detect_labels(
        Image={"Bytes": imagedata,}, MaxLabels=5, MinConfidence=70,
    )

    message = []

    for i in response["Labels"]:
        message.append(f'{i["Name"]} ({round(i["Confidence"],0)}%)')

    return True, ", ".join(message)


def submit_to_rekognition_celebrity(
    config: ConfigParser, imagedata
) -> Tuple[bool, str]:

    client = boto3.client(
        "rekognition",
        region_name=config["aws"]["region"],
        aws_access_key_id=config["aws"]["access_key"],
        aws_secret_access_key=config["aws"]["secret_key"],
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
