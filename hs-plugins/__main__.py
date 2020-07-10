import logging
import grpc
import os


from urllib.parse import urlparse
from urlextract import URLExtract

from rekognition import analyze_celebrity, analyze_url, analyze_image
from interceptor import add_header
import seabird_pb2
import seabird_pb2_grpc


LOG = logging.getLogger("hs-plugins")
log_handler = logging.StreamHandler()
log_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
LOG.addHandler(log_handler)
LOG.setLevel(os.getenv("LOG_LEVEL", "INFO"))


def handle_image(stub, command):
    LOG.debug("handle_image calling analyze_image.")
    message = analyze_image(stub, command.arg)

    if message:
        stub.SendMessage.with_call(
            seabird_pb2.SendMessageRequest(
                channel_id=command.source.channel_id,
                text=f"{command.source.user.display_name}: {message}",
            )
        )


def handle_celebrity(stub, command):
    LOG.debug("celebrity_image calling analyze_celebrity.")
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
        LOG.debug("URL detected: %s", url)
        response = analyze_url(stub, url)
        if response:
            LOG.debug("URL processing successful for %s", url)
            o = urlparse(url)
            LOG.info(o)
            stub.SendMessage.with_call(
                seabird_pb2.SendMessageRequest(
                    channel_id=message.source.channel_id,
                    text=f"{o.netloc}: {response}",
                )
            )
        else:
            LOG.error("URL processing failed for %s", url)


def main():
    LOG.info("Started and opening connection.")
    with grpc.secure_channel(
        os.getenv("SEABIRD_HOST_PORT"), grpc.ssl_channel_credentials(),
    ) as channel:
        channel = grpc.intercept_channel(
            channel,
            add_header(
                "authorization", f'Bearer {os.getenv("SEABIRD_TOKEN")}',
            ),
        )
        LOG.info("Successfully connected.")
        stub = seabird_pb2_grpc.SeabirdStub(channel)
        LOG.info("Monitoring for events.")
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
            LOG.debug("Event received: %s", event.message.text)
            command = event.command
            message = event.message

            if not command.command and not message:
                continue

            extractor = URLExtract(extract_localhost=False)

            if command.command == "inspect_image":
                if command.arg and extractor.has_urls(command.arg):
                    LOG.info(
                        "Image command detected from %s",
                        command.source.user.display_name,
                    )
                    handle_image(stub, command)
                elif not extractor.has_urls(command.arg):
                    LOG.info(
                        "No URL detected from %s",
                        command.source.user.display_name,
                    )
                    stub.SendMessage.with_call(
                        seabird_pb2.SendMessageRequest(
                            channel_id=command.source.channel_id,
                            text=f"{command.source.user.display_name}: Missing URL",
                        )
                    )
                else:
                    LOG.info(
                        "Image command invalid from %s",
                        command.source.user.display_name,
                    )
                    stub.SendMessage.with_call(
                        seabird_pb2.SendMessageRequest(
                            channel_id=command.source.channel_id,
                            text=f"{command.source.user.display_name}: Something's not right",
                        )
                    )
                continue
            elif command.command == "inspect_celebrity":
                if command.arg and extractor.has_urls(command.arg):
                    LOG.info(
                        "Celebrity command detected from %s",
                        command.source.user.display_name,
                    )
                    handle_celebrity(stub, command)
                elif not extractor.has_urls(command.arg):
                    LOG.info(
                        "No URL detected from %s",
                        command.source.user.display_name,
                    )
                    stub.SendMessage.with_call(
                        seabird_pb2.SendMessageRequest(
                            channel_id=command.source.channel_id,
                            text=f"{command.source.user.display_name}: Missing URL",
                        )
                    )
                else:
                    LOG.info(
                        "Celebrity command invalid from %s",
                        command.source.user.display_name,
                    )
                    stub.SendMessage.with_call(
                        seabird_pb2.SendMessageRequest(
                            channel_id=command.source.channel_id,
                            text=f"{command.source.user.display_name}: Something's not right",
                        )
                    )
                continue
            elif extractor.has_urls(message.text):
                LOG.info(
                    "Detected link from %s", message.source.user.display_name,
                )
                handle_url(stub, message)
            else:
                continue


main()
