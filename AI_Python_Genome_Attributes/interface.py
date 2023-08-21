"""
This will actually be incharge of designing the levels, sort of.
Still debating if this file should be a class or more jsut a series of functions
"""

from genome import ChildGenome

width = 16
height = 9


class UI_Grid:
    def __init__(self):
        self.genes = ChildGenome()

        self.grid = list()
        for _ in range(height):
            row = list()
            for _ in range(width):
                row.append("-")
            self.grid.append(row)

        self.children = set()

    def __str__(self):
        for row in self.grid:
            print("\n", row)
        return "\n"

    def generate_children(self):
        pass
