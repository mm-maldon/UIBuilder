"""
This will actually be incharge of designing the levels, sort of.
Still debating if this file should be a class or more jsut a series of functions
"""

from genome import ChildGenome
import random
import math

width = 16
height = 9


class UI_Grid:
    def __init__(self):
        self.children = list()
        self.specified_score = (False, -1)
        self.children_len = 0

    def __str__(self):
        curr_ind = 1
        for child in self.children:
            print("Child: ", curr_ind)
            print(child)
            curr_ind += 1
        return ""

    # Access Functions ------------------------------------------------------

    """
    Just returns the amount of children the objects has
    """

    def get_len(self):
        return self.children_len

    """
    Just loads a new batch of children, perferabbly to a new UI_Grid object
    """

    def load_children(self, new_children):
        self.children_len = len(new_children)
        self.children = new_children

    def get_children(self):
        return self.children

    """
    Just an idea, but this perhaps one way we could generate children with ...
    ... the desired score of a fitness function
    """

    def desired_UI(self, num_val):
        self.specified_score = (True, num_val)

    # Generate Functions ----------------------------------------------------

    """
    Literally just generate the initial set of children to start the cycle of offspring
    """

    def generate_initial_children(self):
        self.children_len = 10
        for _ in range(10):
            self.children.append(ChildGenome())

    """
    Generates children from the new set of parents that were generated in previous iterations
    """

    def generate_new_children(self):
        new_children = list()
        past_couples = set()
        for par_A in self.children:
            for par_B in self.children:
                if par_A != par_B:
                    if (par_A, par_B) not in past_couples:
                        new_child = ChildGenome()
                        new_child.load_parents((par_A, par_B))
                        new_child.inherit_assets()
                        new_children.append(new_child)
                        past_couples.add((par_A, par_B))
                        past_couples.add((par_B, par_A))

        return new_children

    """
    Just loads the user's specified assets into the each child's assets dictionary
    """

    def load_assets(self, tmp_list):
        for child in self.children:
            child.load_traits(tmp_list)

    """
    There's a 10% chance that alters a child's asset's value
    """

    def mutate_children(self):
        for child in self.children:
            mutateChance = round(random.random(), 2)
            # print("Percentage: ", mutateChance)
            if mutateChance <= 0.10:
                child.mutate_assets()

    def create_grids(self):
        for child in self.children:
            if len(child.get_parents()) == 2:
                child.merge_grids()
            else:
                child.produce_grid()

    def grid_to_txt(self):
        ind = 1
        for child in self.children:
            string = str(ind)
            title = "Child_Layout_" + string + ".txt"
            my_list = child.explore_grid()
            with open(title, "w") as f:
                # my_list = ChildGenome.explore_grid(child)

                # print(my_list)
                # list_string = str(my_list)
                for item in my_list:
                    f.write(str(item[0]))
                    f.write(",")
                    f.write(str(item[1][0]))
                    f.write(",")
                    f.write(str(item[1][1]))
                    f.write("\n")
                f.close()
            ind += 1

    # Fitness Functions------------------------------------------------------

    """
    Returns the distance between two points
    """

    def Dijkstra_fcn(self, coordA, coordB):
        distance = 0

        Y = coordA[0] + coordB[0]
        X = coordA[1] + coordB[1]

        XY = (X * X) + (Y * Y)
        distance = math.sqrt(XY)

        return distance

    """
    Checks if a coordinate is in the center of the grid
    """

    def in_center(self, coord):
        X = coord[1]
        Y = coord[0]

        boolX = False
        boolY = False

        if X in range(5, 12):
            boolX = True
        if Y in range(4, 6):
            boolY = True

        if boolX == True and boolY == True:
            return True
        else:
            return False

    """
    Meant to check if a coordinate is on the edges of the screen
    Returns True if they're on the edge, False if not
    """

    def in_edges(self, coord):
        X = coord[1]
        Y = coord[0]
        if X == 0 or X == 15:
            return True
        if Y == 0 or Y == 8:
            return True

        return False

    """
    Calculates the fitness level of the given child
    NOTE: We never subtract constant numbers from the level, we do recipricals
    """

    def calc_fitness(self, child):
        centerCoord = (7, 4)
        fitness = 0

        assets = child.get_assets()

        for item, val in assets.items():
            # print("curr item: ", item, " = ", val)
            appendVal = val
            itemQuad = child.get_item_quad(item)
            itemCoord = child.get_item_coord(item)

            if self.in_edges(itemCoord):
                appendVal += 0.50
            else:
                appendVal += 1.50

            dist = self.Dijkstra_fcn(itemCoord, centerCoord)
            if self.in_center(itemCoord):
                if dist > 0:
                    appendVal -= 1 / dist
                else:
                    appendVal -= 1
            else:
                appendVal += dist

            appendVal *= 1 / itemQuad
            # print(item, ": ", appendVal)
            fitness += appendVal

        child.set_fitness(fitness)

    # Debugging Functions ---------------------------------------------------

    def print_child_assets(self):
        curr_ind = 0
        for child in self.children:
            print("Child ", curr_ind + 1)
            child.print_assets()
            curr_ind += 1
