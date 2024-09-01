import typing
from enum import Enum

from .areel import AReel


class InductorReel(AReel):
    inductance_henries: int
    tolerance: typing.Optional[float]
    shielded: typing.Optional[bool]

    @property
    def part_type(self) -> str:
        return "inductor"
