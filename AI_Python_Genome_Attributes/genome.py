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
        self.parents = tuple()

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
        if len(self.parents) != 2:
            for item, val in self.assets.items():
                rand_val = random.randint(1, self.assets_len)
                self.assets[item] = round((val * rand_val), 2)
        else:
            parent_A = self.parents[0].get_assets()
            parent_B = self.parents[1].get_assets()

            for item, value_A in parent_A.items():
                value_B = parent_B[item]
                self.assets[item] = round(((value_A + value_B) / 2), 2)

    # Access Functions ------------------------------------------------------

    """
    Literally just loads parents into the new child
    """

    def load_parents(self, new_parents):
        self.parents = new_parents

    """
    An access function to get the parents assets dicitonary with their unique values
    """

    def get_assets(self):
        return self.assets

    """
    A helper function that can be called to return the asset with the highest value
    """

    def max_asset(self):
        max_value = 0 - 1
        max_item = None
        for item, value in self.assets.items():
            if value > max_value:
                max_item = item

        if max_value > (0 - 1):
            return max_item
        else:
            return False

    # Template Functions ----------------------------------------------------

    """
    This is a function that places items within the range of the upper left coordinate of the screen
    """

    def upper_left(self, amount):
        for _ in range(amount):
            rand = random.randint(1, 100)

            for Y in range(int(height / 2)):
                for X in range(int(width / 2)):
                    if self.grid[Y][X] == "-":
                        item = self.max_asset()
                        if (item != False) and (rand < 50):
                            self.grid[Y][X] = item
                            break
                    break
                break

    def upper_right(self, amount):
        for _ in range(amount):
            rand = random.randint(1, 100)

            for Y in range(int(height / 2)):
                for X in range(int(width / 2), width):
                    if self.grid[Y][X] == "-":
                        item = self.max_asset()
                        if (item != False) and (rand < 50):
                            self.grid[Y][X] = item
                            break
                    break
                break

    def lower_right(self, amount):
        for _ in range(amount):
            rand = random.randint(1, 100)

            for Y in range(int(height / 2), height):
                for X in range(int(width / 2), width):
                    if self.grid[Y][X] == "-":
                        item = self.max_asset()
                        if (item != False) and (rand < 50):
                            self.grid[Y][X] = item
                            break
                    break
                break

    def lower_left(self, amount):
        for _ in range(amount):
            rand = random.randint(1, 100)

            for Y in range(int(height / 2), height):
                for X in range(int(width / 2)):
                    if self.grid[Y][X] == "-":
                        item = self.max_asset()
                        if (item != False) and (rand < 50):
                            self.grid[Y][X] = item
                            break
                    break
                break

    # Debugging Functions ---------------------------------------------------

    """
    Another debugging function, mostly to check our assets for each child
    """

    def print_assets(self):
        print("{")
        for item, value in self.assets.items():
            print(item, " : ", value)
        print("}")
