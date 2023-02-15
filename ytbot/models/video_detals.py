from typing import NamedTuple
from datetime import date, timedelta

from ytbot.models.like_count import LikeCount


class VideoDetails(NamedTuple):
    title: str
    channel_name: str
    upload_date: date
    duration: timedelta
    view_count: int
    like_count: LikeCount
    dislike_count: LikeCount

    def __str__(self):
        return "Video details:\n\t" + "\n\t".join([
            f"Title: '{self.title}'",
            f"Channel name: '{self.channel_name}'",
            f"Upload date: {self.upload_date}",
            f"Duration: {self.duration}",
            f"View count: {self.view_count}",
            f"Like count: {self.like_count}",
            f"Dislike count: {self.dislike_count}"
        ])
