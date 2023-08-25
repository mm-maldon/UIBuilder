# genome.py
Meant as a class, representing the genome for each individual UI.
- __init__(self)
    - self.assets : a dictionary holding assets and numerical values
    - self.fitness : the child's numerical fitness level
    - self.assets_len : literally just the number of assets 
    - self.grid_len : is the number of elements currently placed on the grid
    - self.parents : the child's parents
    - self.grid : a 16X9 grid that's initialized with only empty spaces
- __str__(self)
    - Prints out the assets dicitonary, mostly used for debugging
## Generate Functions
- load_traits(self)
    - Literally just to load traits and specify assets
    - Will only sustain the assets the user specifies, nothing more, nothing less
    - The value for the assets are heirarchal, meaning their value is dependent on the amount of inputs and the order of input.
- mutate_assets(self)
    - There's a 50% chance that the child's assets' either:
        - All change value
        - Or a new item with a value of 0.1 is added
- inherit_assets(self)
    - A child inherits traits from both parents, specifically assets
    - If the parent's have any differences, then the child has a 25% of inherting that's parents asset
- load_parents(self, new_parents)
    - new_parents :  a tuple of two other ChildGenome() objects
    - Literally just loads the tuple to the variable self.parents
## Access Functions
- get_assets(self)
    - Just returns the child's current assets when called
- get_fitness(self)
    - Just returns the child's current fitness level
- get_grid(self)
    - Returns the child's current grid
- max_asset(self)
    - This function just returns the child's asset with the highest value
- curr_max(self)
    - This function returns the asset with thenhighest value that has NOT been placed yet.
## Template Functions
- upper_left(self, amount)
    - amount : the number of objects specified to go in the upper left quadrant
- upper_right(self, amount)
    - amount : the number of objects specified to go in the upper right quadrant
- lower_right(self, amount)
    - amount : the number of objects specified to go in the lower right quadrant
- lower_left(self, amount)
    - amount : the number of objects specified to go in the lower left quadrant
- place_quad(self, quad, item)
    - quad : the quadrant the user wants to place assets into
    - item : the asset the user wnat to place in the specified quadrant
    - Places an item in the specified quadrant requested by the user
## Grid Functions
- produce_grid(self)
    - More for the initialziation, but it makes basic grids for the initial set of children
    - The function evenly places the number of elements between the four quadrants
- merge_grids(self)
    - Literally just merges grids from the child's parents to make a new one 
## Debugging Functions
- print_assets(self)
    - Just prints the child's current assets
    - This is more meant for beugging
- check_quadrant(self, item, quad)
    - item : the item you want to check in the selected quadrant
    - quad : the quadrant you want to check
    - Checks if the item you want to place already exists in that quadrant of the grid
- check_grid(self, item)
    - item : the item you want if it already exists in the child's grid
    - Checks if the item you want to place already exists in the entire grid


# interface_class.py
The class, the object that acutally builds the UI and creates offspring.
- __init__(self)
    - self.children : a list of the UI_Grids ChildGenome objects
    - self.specified_score : stores the fitness value from the child chosen by the user
    - self.children_len : the number of children the UI_Grid object holds
- __str__(self)
    - Prints out the graphs of every child
## Access Functions
- get_len(self)
    - returns self.children_len
- self.load_children(self, new_children)
    - new_children : a list of new ChildGenome objects
    - Meant to load a list of new children into the current or a new UI_Grid object
- desired_UI(self, num_val)
    - num_val : the fitness value from the chosen child
    - Literally just stores the fitness value we want to reach/excede in the next iteration
## Generate Functions
- generate_initial_children(self)
    - Generates 10 random children from the loaded assets given by the user
- generate_new_children(self)
    - Generates new children from the current objects list of parents/children
    - Returns a list of the newly generated children
- load_assets(self, tmp_list)
    - tmp_list : a list of assets the user wants implemented in the UI
    - Only loads the assets into each child's asset dictionary
- mutate_children(self)
    - There's a 10% chance that a children in the UI_Grids chld list get's mutated by the mutate_assets function
- create_grid(self)
    - Generates a grid for every child stored in the UI_Grid object
## Fitnes Functions
- calc_fitness(self)
    - Is meant to calcualte the fitness value for every child stored
## Debugging Functions
- print_child_assets(self)
    - Just prints out the assets dictionary of every child stored

# genome_client.py
Meant to be where we actually create and alter the child genome objects.

Currently used for debugging, works as intended, or more for what I intended.