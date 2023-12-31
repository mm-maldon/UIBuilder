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
import math

all_assets = [
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

width = 16
height = 9


class ChildGenome:
    def __init__(self):
        self.assets = dict()  # This will hold the assets and their heirarchal value
        self.asset_locations = (
            dict()
        )  # litterally just stores the locatin of each asset
        self.fitness = 0  #  The current childs genetic value, the value in which to select valid offspring
        self.assets_len = 0
        self.grid_len = 0
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

    # Generate Functions-----------------------------------------------------

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

    def mutate_assets(self):
        coinFlip = random.random()

        if self.grid_len == self.assets_len:
            if coinFlip <= 0.75:
                for item, val in self.assets.items():
                    rand_val = random.randint(1, self.assets_len)
                    self.assets[item] = round((val * rand_val), 2)
        else:
            if coinFlip <= 0.5:
                for item, val in self.assets.items():
                    rand_val = random.randint(1, self.assets_len)
                    self.assets[item] = round((val * rand_val), 2)
            else:
                tmpBool = True
                while tmpBool:
                    newItem = random.choice(all_assets)
                    if newItem not in self.assets.keys() and newItem != "-":
                        self.assets[newItem] = 0.1
                        self.assets_len += 1
                        tmpBool = False

    """
    This is meant to actually produce a new dictionary of assets depedning on the parents
    """

    def inherit_assets(self):
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
            if itemA not in assetsB:
                if chanceA <= 0.25:
                    self.assets[itemA] = round(((parentA[itemA]) / 2), 2)
                    self.assets_len += 1
            else:
                mutualTraits.add(itemA)

        for itemB in assetsB:
            chanceB = random.random()
            if itemB not in assetsA:
                if chanceB <= 0.25:
                    self.assets[itemB] = round(((parentB[itemB]) / 2), 2)
                    self.assets_len += 1
            else:
                mutualTraits.add(itemB)

        for itemM in mutualTraits:
            valA = parentA[itemM]
            valB = parentB[itemM]
            self.assets[itemM] = round(((valA + valB) / 2), 2)
            self.assets_len += 1

    """
    Literally just loads parents into the new child
    """

    def load_parents(self, new_parents):
        self.parents = new_parents

    # Access Functions ------------------------------------------------------

    """
    An access function to get the parents assets dicitonary with their unique values
    """

    def get_assets(self):
        return self.assets

    """
    An access function to get the child'scurrent fitness level
    """

    def get_fitness(self):
        return self.fitness

    """
    Sets the fitness to the value specified by the user
    """

    def set_fitness(self, val):
        self.fitness = val

    """
    Returns the child's current grid
    """

    def get_grid(self):
        return self.grid

    """
    Returns the tuple of the child's parents
    """

    def get_parents(self):
        return self.parents

    """
    Returns the coordinates of the specified item, if it exists in the grid
    """

    def get_item_coord(self, item):
        if self.check_grid(item):
            return self.asset_locations[item]
        return False

    """
    Returns the specified items quadrant location
    """

    def get_item_quad(self, item):
        quads = [1, 2, 3, 4]
        for i in quads:
            if self.check_quadrant(item, i):
                return i
        return False

    """
    A helper function that can be called to return the asset with the highest value
    """

    def max_asset(self):
        max_value = 0 - 1
        max_item = None
        for item, value in self.assets.items():
            if value > max_value:
                max_item = item
                max_value = value

        # print("max val: ", max_value)
        if max_value > (0 - 1):
            return max_item
        else:
            return False

    """
    Returns the next item, that's not on the grid" with the highest value
    """

    def curr_max(self):
        max_val = 0 - 1
        max_item = False

        for item, value in self.assets.items():
            tmpBool = self.check_grid(item)
            if not tmpBool:
                if value > max_val:
                    max_item = item
                    max_val = value

        return max_item

    # Template Functions ----------------------------------------------------

    """
    This is a function that places items within the range of the upper left coordinate of the screen
    """

    def upper_left(self, amount):
        for _ in range(amount):
            placeBool = True
            item = self.curr_max()
            # print("item up: ", item)
            if item != False:
                while placeBool == True:
                    rand = random.random()
                    Y = random.randint(0, int(height / 2) - 1)
                    X = random.randint(0, int(width / 2) - 1)
                    if self.grid[Y][X] == "-":
                        if round(rand, 2) <= 0.75:
                            self.grid[Y][X] = item
                            self.asset_locations[item] = (Y, X)
                            self.grid_len += 1
                            placeBool = False

    def upper_right(self, amount):
        for _ in range(amount):
            placeBool = True
            item = self.curr_max()
            if item != False:
                while placeBool == True:
                    rand = random.random()
                    Y = random.randint(0, int(height / 2) - 1)
                    X = random.randint(int(width / 2), (width - 1))
                    if self.grid[Y][X] == "-":
                        if round(rand, 2) <= 0.75:
                            self.grid[Y][X] = item
                            self.asset_locations[item] = (Y, X)
                            self.grid_len += 1
                            placeBool = False

    def lower_right(self, amount):
        for _ in range(amount):
            placeBool = True
            item = self.curr_max()
            # print("item low: ", item)
            if item != False:
                while placeBool == True:
                    rand = random.random()
                    Y = random.randint(int(height / 2), (height - 1))
                    X = random.randint(int(width / 2), (width - 1))
                    if self.grid[Y][X] == "-":
                        if round(rand, 2) <= 0.75:
                            self.grid[Y][X] = item
                            self.asset_locations[item] = (Y, X)
                            self.grid_len += 1
                            placeBool = False

    def lower_left(self, amount):
        for _ in range(amount):
            placeBool = True
            item = self.curr_max()
            if item != False:
                while placeBool == True:
                    rand = random.random()
                    Y = random.randint(int(height / 2), (height - 1))
                    X = random.randint(0, int(width / 2) - 1)
                    if self.grid[Y][X] == "-":
                        if round(rand, 2) <= 0.75:
                            self.grid[Y][X] = item
                            self.asset_locations[item] = (Y, X)
                            self.grid_len += 1
                            placeBool = False

    """
    This is similar to the above functions, except this is to specifically...
    ... add an element to a specified quadrant
    """

    def place_quad(self, quad, item):
        itemBool = self.check_grid(item)
        X = 0 - 1
        Y = 0 - 1
        if not itemBool:
            # tmpBool = True
            # while tmpBool == True:
            while True:
                rand = random.random()
                if quad == 1:
                    Y = random.randint(0, int(height / 2) - 1)
                    X = random.randint(0, int(width / 2) - 1)
                elif quad == 2:
                    Y = random.randint(0, int(height / 2) - 1)
                    X = random.randint(int(width / 2), (width - 1))
                elif quad == 3:
                    Y = random.randint(int(height / 2), (height - 1))
                    X = random.randint(int(width / 2), (width - 1))
                elif quad == 4:
                    Y = random.randint(int(height / 2), (height - 1))
                    X = random.randint(0, int(width / 2) - 1)
                else:
                    return False

                if self.grid[Y][X] == "-":
                    self.grid[Y][X] = item
                    self.asset_locations[item] = (Y, X)
                    self.grid_len += 1
                    # tmpBool = False
                    return True
        return False

    # Grid Functions --------------------------------------------------------

    """
    Literally just produces a random grid for the initial pair of children
    """

    def produce_grid(self):
        while self.grid_len < self.assets_len:
            amountItems = math.ceil(self.assets_len / 4)
            tmpPercent = random.random()

            if tmpPercent <= 0.25:
                self.upper_left(amountItems)
                self.upper_right(amountItems)
                self.lower_right(amountItems)
                self.lower_left(amountItems)
            elif tmpPercent <= 0.50:
                self.lower_left(amountItems)
                self.upper_left(amountItems)
                self.upper_right(amountItems)
                self.lower_right(amountItems)
            elif tmpPercent <= 0.75:
                self.lower_right(amountItems)
                self.lower_left(amountItems)
                self.upper_left(amountItems)
                self.upper_right(amountItems)
            else:
                self.upper_right(amountItems)
                self.lower_right(amountItems)
                self.lower_left(amountItems)
                self.upper_left(amountItems)

    """
    A function that was constently getting repeated in it's parent function
    """

    def merge_grid_helper(self, parent, item):
        itemChance = round(random.random(), 2)

        if itemChance < 0.75:
            coord = parent.get_item_coord(item)
            if self.grid[coord[0]][coord[1]] == "-":
                self.grid[coord[0]][coord[1]] = item
                self.asset_locations[item] = coord
                self.grid_len += 1
            else:
                loc = parent.get_item_quad(item)
                self.place_quad(loc, item)
        else:
            loc = parent.get_item_quad(item)
            self.place_quad(loc, item)

    """
    Creates a new grid by merging aspect from it's parents' grids
    """

    def merge_grids(self):
        childAssets = self.get_assets()

        parentA = self.parents[0]
        assetsA = parentA.get_assets()
        keysA = assetsA.keys()

        parentB = self.parents[1]
        assetsB = parentB.get_assets()
        keysB = assetsB.keys()

        for item in childAssets.keys():
            # print("Merge item: ", item)
            itemChance = round(random.random(), 2)
            if (item in keysA) and (item in keysB):
                if assetsA[item] > assetsB[item]:
                    self.merge_grid_helper(parentA, item)
                elif assetsA[item] < assetsB[item]:
                    self.merge_grid_helper(parentB, item)
                else:
                    if itemChance < 0.50:
                        self.merge_grid_helper(parentA, item)
                    else:
                        self.merge_grid_helper(parentB, item)

            elif item in keysA:
                self.merge_grid_helper(parentA, item)

            elif item in keysB:
                self.merge_grid_helper(parentB, item)

            else:
                randLoc = random.choice([1, 2, 3, 4])
                self.place_quad(randLoc, item)

    def mutate_grid(self):
        pass

    """
    def grid_to_txt(self):
        my_list = self.explore_grid()
        with open('gridLayout.txt', 'w') as f:
            for item in my_list:
                f.write(item)
                f.write('\n')
        pass
    """

    # Debugging Functions ---------------------------------------------------

    """
    Another debugging function, mostly to check our assets for each child
    """

    def print_assets(self):
        print("{")
        for item, value in self.assets.items():
            print(item, " : ", value)
        print("}")

    """
    Meant to return the assets and their corresponding coordinates
    """

    def print_assets_coord(self):
        print("{")
        for item, value in self.asset_locations.items():
            print(item, " : ", value)
        print("}")
        return

    """
    Meant to check for duplicate assets in a certain quadrant
    """

    def check_quadrant(self, item, quad):
        yBound = range(0, 0)
        xBound = range(0, 0)

        if quad == 1:
            yBound = range(0, int(height / 2))
            xBound = range(0, int(width / 2))
        elif quad == 2:
            yBound = range(0, int(height / 2))
            xBound = range(int(width / 2), width)
        elif quad == 3:
            yBound = range(int(height / 2), height)
            xBound = range(int(width / 2), width)
        elif quad == 4:
            yBound = range(int(height / 2), height)
            xBound = range(0, int(width / 2))
        else:
            return False

        for Y in yBound:
            for X in xBound:
                if item == self.grid[Y][X]:
                    return True

        return False

    """
    Checks the child's grid for duplicate assets in the entire grid
    """

    def check_grid(self, item):
        for Y in self.grid:
            for X in Y:
                if X == item:
                    return True

        return False

    """
    Iterates through every point on the grid and returns a list containing each point
    """

    def explore_grid(self):
        my_list = list()
        for asset, value in self.asset_locations.items():
            flipped = (value[1], value[0])  # changes from (Y, X) to (X, Y)
            my_list.append((asset, flipped))
        return my_list
