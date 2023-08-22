# genome.py
Meant as a class, representing the genome for each individual UI.
- __init(self)
    - self.assets : a dictionary holding assets and numerical values
    - self.fitness : the child's numerical fitness level
    - self.assets_len : literally just the number of assets 
    - self.parents : the child's parents
    - self.grid : a 16X9 grid that's initialized with only empty spaces
- __str__(self)
    - Prints out the assets dicitonary, mostly used for debugging

- load_traits(self)
    - Literally just to load traits and specify assets
    - Will only sustain the assets the user specifies, nothing more, nothing less
    - The value for the assets are heirarchal, meaning their value is dependent on the amount of inputs and the order of input.
- mutate(self)
    - There's a 50% chance that the child's assets' either:
        - All change value
        - Or a new item with a value of 0.1 is added
- inherit_fcn(self)
    - A child inherits traits from both parents, specifically assets
    - If the parent's have any differences, then the child has a 25% of inherting that's parents asset

- load_parents(self, new_parents)
    - new_parents :  a tuple of two other ChildGenome() objects
    - Literally just loads the tuple to the variable self.parents
- get_assets(self)
    - Just returns the child's current assets when called
- max_asset(self)
    - This function just returns the child's asset with the highest value
- upper_left(self, amount)
    - amount : the number of objects specified to go in the upper left quadrent
- upper_right(self, amount)
    - amount : the number of objects specified to go in the upper right quadrent
- lower_right(self, amount)
    - amount : the number of objects specified to go in the lower right quadrent
- lower_left(self, amount)
    -amount : the number of objects specified to go in the lower left quadrent

- print_assets(self)
    - Just prints the child's current assets
    - This is more meant for beugging


# genome_client.py
Meant to be where we actually create and alter the child genome objects.

Currently used for debugging, works as intended, or more for what I intended.

# interface_class.py
The class, the object that acutally builds the UI and creates offspring.
