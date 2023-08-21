# genome.py
Meant as a class, representing the genome for each individual UI.
- __str__(self)
    - Prints out the assets dicitonary, mostly used for debugging
- load_traits(self)
    - Literally just to load traits and specify assets
    - Will only sustain the assets the user specifies, nothing more, nothing less
    - The value for the assets are heirarchal, meaning their value is dependent on the amount of inputs and the order of input.

# genome_client.py
Meant to be where we actually create and alter the child genome objects.

Currently used for debugging, works as intended, or more for what I intended.

# interface_class.py
The class, the object that acutally builds the UI and creates offspring.

Still debating if this should a class or series of functions.
