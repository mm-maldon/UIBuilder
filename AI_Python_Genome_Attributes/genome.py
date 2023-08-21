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


class ChildGenome:
    def __init__(self):
        self.assets = dict()  # This will hold the assets and their heirarchal value
        self.assets_len = 0  # A variable to hold the number of assets, just to avoid using extra computation time
        self.gene_level = 0  #  The current childs genetic value, the value in which to select valid offspring

    """
    Purely for debuging purposes, just to make sure we have our assets loaded properly
    """

    def __str__(self):
        print("Assets:\n")
        print("{")
        for item, val in self.assets.items():
            print("\n", item, " has the value: ", val)
        return "\n}"

    """
    This function takes in user inputs, the assets the user want's specifically.
    Load those assets into the 'assets' dictionary, and give those assets a heirarchy value
    """

    def load_traits(self):
        max_num_assets = 13
        curr_ind = 13

        while curr_ind > 0:
            user_asset = input("Type Your Specified Asset: >")
            self.assets[user_asset] = curr_ind / max_num_assets

            user_validation = input("Would You Like To Add More Assets [Y/N]: >")
            if user_validation not in ["Y", "N"]:
                while user_validation not in ["Y", "N"]:
                    user_validation = input("Please Type 'Y' or 'N': >")
            if user_validation == "N":
                break

        self.assets_len = len(self.assets)
        curr_ind = len(self.assets)

        for entry in self.assets.keys():
            self.assets[entry] = curr_ind / self.assets_len
            curr_ind -= 1

    """
    This fucntion is only meant to change the values of the assests
    """

    def mutate(self):
        for item, val in self.assets.items():
            rand_val = random.randint(1, self.assets_len)
            self.assets[item] = val * rand_val
