import logging
import grpc
import boto3


import seabird_pb2
import seabird_pb2_grpc


def main():
    host_port = "coded.io:443"
    token = "mytoken"

    with grpc.secure_channel(host_port, grpc.ssl_channel_credentials()) as channel:
        channel = grpc.intercept_channel(
            channel,
            add_header(
                "authorization",
                f"Bearer {token}",
            ),
        )

        stub = seabird_pb2_grpc.SeabirdStub(channel)

