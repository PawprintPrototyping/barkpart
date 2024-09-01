import typing
from abc import ABC, abstractmethod

from attrs import define


@define
class AReel(ABC):
    """Abstract class for a reel of reels"""

    id: int
    """UID for the reel, so the database is happy"""
    count: int
    """Number of reels on this reel"""
    footprint: str
    """The type of footprint for the part"""
    reorder_url: typing.Optional[str]
    """URL for reordering the part"""
    part_number: typing.Optional[int]
    """Part number (optional)"""

    @property
    @abstractmethod
    def part_type(self) -> str:
        """Read only part type, for categorizing reels. Should always return a lowercase string"""
        return "undefined"
