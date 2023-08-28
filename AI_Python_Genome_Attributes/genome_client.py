from genome import ChildGenome
from interface import UI_Grid

import random

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

"""
Generating the first New Generation
"""
new_generation = UI_A.generate_new_children()
UI_B = UI_Grid()
UI_B.load_children(new_generation)
UI_B.mutate_children()
UI_B.create_grids()

for child in UI_B.get_children():
    UI_B.calc_fitness(child)
UI_B.grid_to_txt()

favChoice = int(input("Favorite UI Template: "))
chosenChild = UI_B.get_children()[favChoice - 1]
chosenFit = chosenChild.get_fitness()


"""
Generating a New Generation
"""
listOne = UI_B.get_children()
listOne.sort(key=lambda x: x.get_fitness())

listTwo = list()
currInd = 0
for child in listOne:
    if child.get_fitness() >= chosenFit and currInd < 10:
        listTwo.append(child)
        currInd += 1

while len(listTwo) < 10:
    rand = random.choice(listOne)
    if rand not in listTwo:
        listTwo.append(rand)

UI_C = UI_Grid()
UI_C.load_children(listTwo)
UI_C.mutate_children()
UI_C.create_grids()

for child in UI_C.get_children():
    UI_C.calc_fitness(child)
UI_C.grid_to_txt()

favChoice = int(input("Favorite UI Template: "))
chosenChild = UI_C.get_children()[favChoice - 1]
chosenFit = chosenChild.get_fitness()

"""
Generating the third generation
"""
listThree = UI_C.get_children()
listThree.sort(key=lambda x: x.get_fitness())

listFour = list()
currInd = 0
for child in listFour:
    if child.get_fitness() >= chosenFit and currInd < 10:
        listFour.append(child)
        currInd += 1

while len(listFour) < 10:
    rand = random.choice(listOne)
    if rand not in listFour:
        listTwo.append(rand)

UI_D = UI_Grid()
UI_D.load_children(listTwo)
UI_D.mutate_children()
UI_D.create_grids()

for child in UI_D.get_children():
    UI_D.calc_fitness(child)
UI_D.grid_to_txt()

favChoice = int(input("Favorite UI Template: "))
chosenChild = UI_D.get_children()[favChoice - 1]
chosenFit = chosenChild.get_fitness()

"""
Generating the last generation
"""

listFive = UI_B.get_children()
listFive.sort(key=lambda x: x.get_fitness())

listFive = list()
currInd = 0
for child in listFour:
    if child.get_fitness() >= chosenFit and currInd < 10:
        listFive.append(child)
        currInd += 1

while len(listFive) < 10:
    rand = random.choice(listFour)
    if rand not in listFive:
        listFive.append(rand)

UI_E = UI_Grid()
UI_E.load_children(listTwo)
UI_E.mutate_children()
UI_E.create_grids()

for child in UI_E.get_children():
    UI_E.calc_fitness(child)
UI_E.grid_to_txt()


# for _ in range(3):
#     """
#     Your Code Here
#     """

#     pass
