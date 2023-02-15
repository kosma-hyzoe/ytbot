from datetime import datetime, date, timedelta

import humanfriendly

from ytbot.models.like_count import LikeCount

YT_DATE_FORMAT = "%b %d, %Y"


def parse_video_duration(duration: str) -> timedelta:
    if ':' in duration:
        duration_parts = duration.split(':')
        if len(duration_parts) == 2:
            hours, minutes, seconds = 0, int(duration_parts[0]), int(duration_parts[1])
        elif len(duration_parts) == 3:
            hours, minutes, seconds = int(duration_parts[0]), int(duration_parts[1]), int(duration_parts[2])
        else:
            raise ValueError(f"Wrong duration format: {duration}")
    else:
        seconds = int(duration)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

    return timedelta(hours=hours, minutes=minutes, seconds=seconds)


def parse_view_count(view_count: str) -> int:
    view_count = view_count[:view_count.index("views")].strip()
    return int(view_count.replace(",", "_"))


def parse_like_count(like_count: str) -> LikeCount:
    if not like_count:
        return LikeCount(0, approximated=False)
    try:
        return LikeCount(int(like_count), approximated=False)
    except ValueError:
        return LikeCount(humanfriendly.parse_size(like_count), approximated=True)


def parse_upload_date(upload_date: str) -> date:
    if "Premiered" in upload_date:
        upload_date = upload_date.replace("Premiered", "").strip()
    return datetime.strptime(upload_date, YT_DATE_FORMAT).date()
