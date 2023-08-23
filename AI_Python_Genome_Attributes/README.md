# genome.py
Meant as a class, representing the genome for each individual UI.
- __init__(self)
    - self.assets : a dictionary holding assets and numerical values
    - self.fitness : the child's numerical fitness level
    - self.assets_len : literally just the number of assets 
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
- max_asset(self)
    - This function just returns the child's asset with the highest value
## Template Functions
- upper_left(self, amount)
    - amount : the number of objects specified to go in the upper left quadrant
- upper_right(self, amount)
    - amount : the number of objects specified to go in the upper right quadrant
- lower_right(self, amount)
    - amount : the number of objects specified to go in the lower right quadrant
- lower_left(self, amount)
    - amount : the number of objects specified to go in the lower left quadrant
## Grid Functions
- produce_grid(self)
    - More for the initialziation, but it makes basic grids for the initial set of children
- merge_grids(self)
    - Literally just merges grids from the child's parents to make a new one 
## Debugging Functions
- print_assets(self)
    - Just prints the child's current assets
    - This is more meant for beugging
- check_quadrant(self, item, quad)
    - item : the item you want to check in the selected quadrant
    - quad : the quadrant you want to check
- check_grid(self, item)
    - item : the item you want if it already exists in the child's grid


# genome_client.py
Meant to be where we actually create and alter the child genome objects.

Currently used for debugging, works as intended, or more for what I intended.

# interface_class.py
The class, the object that acutally builds the UI and creates offspring.
