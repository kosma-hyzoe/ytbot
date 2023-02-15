from typing import NamedTuple


class LikeCount(NamedTuple):
    count: int
    approximated: bool

    def __str__(self):
        return f"over {self.count}" if self.approximated else str(self.count)
