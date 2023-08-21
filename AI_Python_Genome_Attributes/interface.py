"""
This will actually be incharge of designing the levels, sort of.
Still debating if this file should be a class or more jsut a series of functions
"""

from genome import ChildGenome

width = 16
height = 9


class UI_Grid:
    def __init__(self):
        self.children = list()
        for _ in range(10):
            self.children.append(ChildGenome())

    def __str__(self):
        for child in self.children:
            print(child)
        return ""

    def load_assets(self, tmp_list):
        for child in self.children:
            child.load_traits(tmp_list)
            child.mutate()

    # Debugging Functions ---------------------------------------------------

    def print_child_assets(self):
        curr_ind = 0
        for child in self.children:
            print("Child ", curr_ind + 1)
            child.print_assets()
            curr_ind += 1
