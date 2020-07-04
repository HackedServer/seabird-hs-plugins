import logging
import grpc
import os


from urllib.parse import urlparse
from urlextract import URLExtract

from rekognition import analyze_image, analyze_celebrity, analyze_url
from interceptor import add_header
import seabird_pb2
import seabird_pb2_grpc


def handle_image(stub, command):
    message = analyze_image(stub, command.arg)

    stub.SendMessage.with_call(
        seabird_pb2.SendMessageRequest(
            channel_id=command.source.channel_id,
            text=f"{command.source.user.display_name}: {message}",
        )
    )


def handle_celebrity(stub, command):
    message = analyze_celebrity(stub, command.arg)

    stub.SendMessage.with_call(
        seabird_pb2.SendMessageRequest(
            channel_id=command.source.channel_id,
            text=f"{command.source.user.display_name}: {message}",
        )
    )


def handle_url(stub, message):
    extractor = URLExtract()

    urls = extractor.find_urls(message.text, only_unique=True)

    for url in urls:
        response = analyze_url(stub, url)
        if response:
            o = urlparse(url)

            stub.SendMessage.with_call(
                seabird_pb2.SendMessageRequest(
                    channel_id=message.source.channel_id,
                    text=f"{o.scheme}://{o.netloc}/: {response}",
                )
            )


def main():
    with grpc.secure_channel(
        os.getenv("SEABIRD_HOST_PORT"),
        grpc.ssl_channel_credentials(),
    ) as channel:
        channel = grpc.intercept_channel(
            channel,
            add_header(
                "authorization",
                f'Bearer {os.getenv("SEABIRD_TOKEN")}',
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
            message = event.message

            if not command or not message:
                continue

            extractor = URLExtract()

            if command.command == "inspect_image":
                if command.arg:
                    handle_image(stub, command)
                else:
                    stub.SendMessage.with_call(
                        seabird_pb2.SendMessageRequest(
                            channel_id=command.source.channel_id,
                            text=f"{command.source.user.display_name}: Missing URL",
                        )
                    )
                continue
            elif command.command == "inspect_celebrity":
                if command.arg:
                    handle_celebrity(stub, command)
                else:
                    stub.SendMessage.with_call(
                        seabird_pb2.SendMessageRequest(
                            channel_id=command.source.channel_id,
                            text=f"{command.source.user.display_name}: Missing URL",
                        )
                    )
                continue
            elif extractor.has_urls(message.text):
                handle_url(stub, message)
            else:
                continue


main()
