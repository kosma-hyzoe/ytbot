from typing import NamedTuple


class VideoDetails(NamedTuple):
    title: str
    channel_name: str
    upload_date: str
    duration: str
    view_count: str
    like_count: str
    dislike_count: str

    def __str__(self):
        return "\n".join([
            f"Title: '{self.title}'",
            f"Channel name: '{self.channel_name}'",
            f"Upload date: '{self.upload_date}'",
            f"Duration: {self.duration}",
            f"View count: {self.view_count}",
            f"Like count: '{self.like_count}'",
            f"Dislike count: '{self.dislike_count}'"
        ])
