import logging
import grpc
import configparser

from rekognition import analyze_image, analyze_celebrity
from interceptor import add_header
import seabird_pb2
import seabird_pb2_grpc


def get_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def handle_image(stub, command):
    config = get_config("config.ini")

    message = analyze_image(stub, config, command.arg)

    stub.SendMessage.with_call(
        seabird_pb2.SendMessageRequest(
            channel_id=command.source.channel_id,
            text=f"{command.source.user.display_name}: {message}",
        )
    )

def handle_celebrity(stub, command):
    config = get_config("config.ini")

    message = analyze_celebrity(stub, config, command.arg)

    stub.SendMessage.with_call(
        seabird_pb2.SendMessageRequest(
            channel_id=command.source.channel_id,
            text=f"{command.source.user.display_name}: {message}",
        )
    )

def main():

    config = get_config("config.ini")

    print(config["DEFAULT"]["seabird_grpc_hostport"])
    print(config["DEFAULT"]["seabird_grpc_token"])

    with grpc.secure_channel(
        config["DEFAULT"]["seabird_grpc_hostport"],
        grpc.ssl_channel_credentials(),
    ) as channel:
        channel = grpc.intercept_channel(
            channel,
            add_header(
                "authorization",
                f'Bearer {config["DEFAULT"]["seabird_grpc_token"]}',
            ),
        )

        stub = seabird_pb2_grpc.SeabirdStub(channel)

        for event in stub.StreamEvents(
            seabird_pb2.StreamEventsRequest(
                commands={
                    "inspect_image": seabird_pb2.CommandMetadata(
                        name="inspect_image",
                        short_help="AWS Rekognition to analyze an image",
                        full_help="Analyze an image's content",
                    ),
                    "inspect_celebrity": seabird_pb2.CommandMetadata(
                        name="inspect_image",
                        short_help="AWS Rekognition to analyze an image",
                        full_help="Analyze an image's content",
                    ),
                },
            )
        ):
            command = event.command
            if not command:
                continue

            if command.command == "inspect_image":
                if command.arg:
                    handle_image(stub, command)
                else:
                    stub.SendMessage.with_call(
                        seabird_pb2.SendMessageRequest(
                            channel_id=command.source.channel_id,
                            text=f"{command.source.user.display_name}: HS test",
                        )
                    )
            elif command.command == "inspect_celebrity":
                if command.arg:
                    handle_celebrity(stub, command)
                else:
                    stub.SendMessage.with_call(
                        seabird_pb2.SendMessageRequest(
                            channel_id=command.source.channel_id,
                            text=f"{command.source.user.display_name}: HS test",
                        )
                    )
            else:
                continue


main()
