from dataclasses import dataclass


@dataclass(frozen=True)
class Escada:
    def __init__(self, ladder_height_mm):
        self.ladder_height_mm = ladder_height_mm

        self.ladder_total_height_mm = self.ladder_height_mm + 1260
        self.cage_height_mm = self.ladder_total_height_mm - 2000

        self.steps_num = round(self.ladder_height_mm / 280)
        self.vert_cage_elements_num = 5
        self.hori_cage_elements_num = round(self.cage_height_mm / 800)
