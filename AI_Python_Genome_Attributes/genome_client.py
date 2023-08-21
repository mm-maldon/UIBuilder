# from genome import ChildGenome
from interface import UI_Grid

UI = UI_Grid()
# print(UI)
UI.load_assets(["a", "b", "c", "d", "e"])

UI.print_child_assets()
