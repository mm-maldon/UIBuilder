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

all_assets = set(
    [
        "C",  # Compass
        "HB",  # Health Bar
        "WS",  # Weapon Sharpness
        "WL",  # Weapom Load
        "EHB",  # Enemy Health Bar
        "PIP_02",  # Palico Item Pickup
        "MM",  # Mini Map
        "LOT",  # Lock-On Toggle
        "CR",  # Combo Reference
        "MO",  # Mission Objective
        "PIP_01",  # Player Item Pickup
        "QI",  # Quick Inventory
        "FA",  # Fling Ammo
        "-",  # Empty Space
    ]
)

width = 16
height = 9


class ChildGenome:
    def __init__(self):
        self.assets = dict()  # This will hold the assets and their heirarchal value
        self.fitness = 0  #  The current childs genetic value, the value in which to select valid offspring
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
    Or, to add a new asset with a value of 0.1 to the dictionary
    The purpose is to to give the user a possibilty that they might not have even thought about
    """

    def mutate(self):
        coinFlip = random.random()

        if coinFlip <= 0.5:
            for item, val in self.assets.items():
                rand_val = random.randint(1, self.assets_len)
                self.assets[item] = round((val * rand_val), 2)
        else:
            currInd = 0
            tmpBool = True
            while (currInd < len(all_assets)) and (tmpBool):
                newItem = all_assets[currInd]
                if newItem not in self.assets.keys():
                    self.assets[newItem] = 0.1
                    tmpBool = False
                currInd += 1

    """
    This is meant to actually produce a new dictionary of assets depedning on the parents
    """

    def inherit_fcn(self):
        parentA = self.parents[0].get_assets()
        assetsA = parentA.keys()
        parentB = self.parents[1].get_assets()
        assetsB = parentB.keys()
        mutualTraits = set()

        # We iterate through both parents assets individually to find any differences
        # If one parent has a trait that other doesn't, then there's a 25% chance ...
        # ... of the child inheriting that trait and half the value
        for itemA in assetsA:
            chanceA = random.random()
            if (itemA not in assetsB) and (chanceA <= 0.25):
                self[itemA] = round(((parentA[itemA]) / 2), 2)
            else:
                mutualTraits.add(itemA)

        for itemB in assetsB:
            chanceB = random.random()
            if (itemB not in assetsA) and (chanceB <= 0.25):
                self[itemB] = round(((parentB[itemB]) / 2), 2)
            else:
                mutualTraits.add(itemB)

        for itemM in mutualTraits:
            valA = parentA[itemM]
            valB = parentB[itemM]
            self.assets[itemM] = round(((valA + valB) / 2), 2)

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
