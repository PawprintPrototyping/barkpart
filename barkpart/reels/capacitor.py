from .areel import AReel


class ResistorReel(AReel):
    ohms: float

    @property
    def part_type(self) -> str:
        return "resistor"