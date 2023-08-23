from genome import ChildGenome
from interface import UI_Grid

UI_A = UI_Grid()
UI_A.generate_initial_children()
# print(UI_A)
UI_A.load_assets(["a", "b", "c", "d", "e"])

UI_A.print_child_assets()

print("Mutate Children\n")
UI_A.mutate_children()
UI_A.print_child_assets()


print("New Children\n")
new_generation = UI_A.generate_new_children()
UI_B = UI_Grid()
UI_B.load_children(new_generation)
UI_B.print_child_assets()
