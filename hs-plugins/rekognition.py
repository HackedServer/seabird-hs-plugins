import boto3
import requests

from configparser import ConfigParser
from typing import Tuple, Any

import seabird_pb2


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

    message = ""

    print(response)
    for i in response["Labels"]:
        message += f'{i["Name"]}: {round(i["Confidence"],2)}, '

    print(message)

    return True, message


def submit_to_rekognition_celebrity(config: ConfigParser, imagedata) -> Tuple[bool, str]:

    client = boto3.client(
        "rekognition",
        region_name=config["aws"]["region"],
        aws_access_key_id=config["aws"]["access_key"],
        aws_secret_access_key=config["aws"]["secret_key"],
    )

    response = client.recognize_celebrities(
        Image={"Bytes": imagedata,},
    )

    message = ""

    print(response)
    for i in response["CelebrityFaces"]:
        message += f'{i["Name"]}, '

    print(message)

    return True, message

def download_image(imageurl: str) -> Tuple[bool, Any]:
    """Downloads the image url and returns a success/fail bool, message or image data"""

    r = requests.get(imageurl, stream=True)

    if r.status_code == requests.codes.ok:
        r.raw.decode_content = True
        return True, r.content
    else:
        return False, "Error message one day"
