import typing
from enum import Enum
from .areel import AReel


class CapacitorMaterials(Enum):
    mlcc = "MLCC"
    tantalum = "TANTALUM"


class CapacitorReel(AReel):
    capacitance_farads: int
    tolerance: typing.Optional[float]
    material: typing.Optional[CapacitorMaterials]

    @property
    def part_type(self) -> str:
        return "capacitor"
