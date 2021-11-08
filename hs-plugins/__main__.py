import asyncio
import logging
import os
from urllib.parse import urlparse

from seabird import Client
from seabird.seabird import CommandMetadata, Event
from urlextract import URLExtract

from rekognition import analyze_celebrity, analyze_image, analyze_url

LOG = logging.getLogger("hs-plugins")
log_handler = logging.StreamHandler()
log_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
LOG.addHandler(log_handler)
LOG.setLevel(os.getenv("LOG_LEVEL", "INFO"))


DEV_CREDS = {
    "token": "LeeG9Gohc9Naejah0eifa7ohGe3ohb5haeshi1eer5phohx6eis5EZoongae",
    "url": "https://seabird-core-dev.elwert.cloud/",
}


async def main():
    LOG.info("Started and opening connection.")
    extractor = URLExtract(extract_localhost=False)
    async with Client(
        os.getenv("SEABIRD_HOST_PORT"),
        os.getenv("SEABIRD_TOKEN"),
    ) as client:
        LOG.info("Successfully connected.")
        LOG.info("Monitoring for events.")
        async for event in client.stream_events(
            commands={
                "inspect_image": CommandMetadata(
                    name="inspect_image",
                    short_help="Inspect an image",
                    full_help="Inspect an image",
                ),
            },
        ):
            if not event.message.text and not event.command.command:
                continue
            r = None
            if event.command.command.lower() == "inspect_image":
                LOG.info(
                    "inspect_image called by %s", event.command.source.user.display_name
                )
                if extractor.has_urls(event.command.arg):
                    LOG.info("URL detected in inspect_image")
                    r = analyze_image(imageurl=event.command.arg)
                else:
                    LOG.info("No image detected in inspect_image")
                    r = "No URL detected"

            elif event.command.command.lower() == "inspect_celebrity":
                LOG.info(
                    "inspect_celebrity called by %s",
                    event.command.source.user.display_name,
                )
                r = analyze_celebrity(imageurl=event.command.arg)
            elif extractor.has_urls(event.message.text):
                LOG.info(
                    "URL detected in message from %s",
                    event.command.source.user.display_name
                    or event.message.source.user.display_name,
                )
                r = analyze_image(imageurl=event.message.text)
                r = None if r == "No image detected." else r

            if r:
                await client.send_message(
                    channel_id=event.command.source.channel_id
                    or event.message.source.channel_id,
                    text=f"{event.command.source.user.display_name or event.message.source.user.display_name}: {r}",
                )


asyncio.run(main())
