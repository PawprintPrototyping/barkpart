import typing

from .areel import AReel


class ResistorReel(AReel):
    ohms: float
    tolerance: typing.Optional[float]

    @property
    def part_type(self) -> str:
        return "resistor"
