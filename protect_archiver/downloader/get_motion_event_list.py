# get motion events list
import logging

from datetime import datetime
from typing import Any
from typing import Counter
from typing import List

import requests

from protect_archiver.dataclasses import Camera
from protect_archiver.dataclasses import MotionEvent


def get_motion_event_list(
    session: Any, start: datetime, end: datetime, camera_list: List[Camera]
) -> List[MotionEvent]:
    motion_events_uri = (
        f"{session.authority}{session.base_path}/events?type=motion"
        f"&start={int(start.timestamp()) * 1000}&end={int(end.timestamp()) * 1000}"
    )
    response = requests.get(
        motion_events_uri,
        cookies={"TOKEN": session.get_api_token()},
        verify=session.verify_ssl,
    )
    if response.status_code != 200:
        print(f"Error while loading motion events list: {response.status_code}")
        return []

    logging.info(f"Successfully retrieved data from {motion_events_uri}")
    # filter ongoing event with no end date https://github.com/danielfernau/unifi-protect-video-downloader/issues/65
    motion_events = filter(lambda motion_event: motion_event["end"], response.json())

    motion_event_list = []
    for motion_event in motion_events:
        motion_event_list.append(
            MotionEvent(
                id=motion_event["id"],
                start=datetime.fromtimestamp(motion_event["start"] / 1000),
                end=datetime.fromtimestamp(motion_event["end"] / 1000),
                camera_id=motion_event["camera"],
                score=motion_event["score"],
                thumbnail_id=motion_event["thumbnail"],
                heatmap_id=motion_event["heatmap"],
            )
        )

    # noinspection PyTypeHints
    event_count_by_camera = Counter(e.camera_id for e in motion_event_list)
    logging.info(
        "Events found:\n{}".format(
            "\n".join(
                f"{event_count_by_camera[x]} motion"
                f" event{'s' if event_count_by_camera[x] > 1 else ''} found for camera"
                f" '{next(c.name for c in camera_list if c.id == x)}' ({x}) between {start} and"
                f" {end}"
                for x in event_count_by_camera
            )
        )
    )

    logging.info(
        f"{len(motion_event_list)} motion events found for all selected cameras between {start} and"
        f" {end}"
    )

    return motion_event_list
