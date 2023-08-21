"""
Valid assets the user can choose/input:
1. Compass
2. Health Bar
3. Weapon Sharpness
4. (Optional) Weapon Load
5. Enemy Health Bar
6. (Optional) Palico Item Pickup
7. Mini Map
8. Lock-On Toggle
9. (Optional) Combo Reference
10. Mission Objective/ Checklist
11. (Optional) Player Item Pickup
12. Quick Inventory
13. Fling Ammo
"""

import random

width = 16
height = 9


class ChildGenome:
    def __init__(self):
        self.assets = dict()  # This will hold the assets and their heirarchal value
        self.gene_level = 0  #  The current childs genetic value, the value in which to select valid offspring
        self.assets_len = 0

        self.grid = list()
        for _ in range(height):
            row = list()
            for _ in range(width):
                row.append("-")
            self.grid.append(row)

    """
    Purely for debuging purposes, just to make sure we are producing a grid properly
    """

    def __str__(self):
        for row in self.grid:
            print("\n", row)
        return ""

    """
    This function takes in user inputs, the assets the user want's specifically.
    Load those assets into the 'assets' dictionary, and give those assets a heirarchy value
    """

    def load_traits(self, tmp_list):
        self.assets_len = len(tmp_list)
        curr_ind = len(tmp_list)

        for item in tmp_list:
            self.assets[item] = round((curr_ind / self.assets_len), 2)
            curr_ind -= 1

    """
    This fucntion is only meant to change the values of the assests
    """

    def mutate(self):
        for item, val in self.assets.items():
            rand_val = random.randint(1, self.assets_len)
            self.assets[item] = round((val * rand_val), 2)

    # Debugging Functions ---------------------------------------------------

    """
    Another debugging function, mostly to check our assets for each child
    """

    def print_assets(self):
        print("{")
        for item, value in self.assets.items():
            print(item, " : ", value)
        print("}")
