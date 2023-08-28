from genome import ChildGenome
from interface import UI_Grid

# UI_A.load_assets(["C", "HB", "LOT", "FA", "WL"])
"""
Getting user input to create am initial set of children
"""
numAssets = int(input("Number of assets: "))
assetList = list()
for _ in range(numAssets):
    tmp = input("Load Asset: ")
    assetList.append(tmp)
UI_A = UI_Grid()
UI_A.generate_initial_children()
UI_A.load_assets(assetList)
UI_A.mutate_children()
UI_A.create_grids()


new_generation = UI_A.generate_new_children()
UI_B = UI_Grid()
UI_B.load_children(new_generation)
UI_B.mutate_children()
UI_B.create_grids()

for child in UI_B.get_children():
    UI_B.calc_fitness(child)
UI_B.grid_to_txt()

for _ in range(3):
    """
    Your Code Here
    """
    pass
