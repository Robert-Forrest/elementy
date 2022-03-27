from .symbols import SYMBOLS
from .density import DENSITY

class Element():

    def __init__(self, number):
        self.number = number
        
        self.symbol = SYMBOLS[self.number-1]

        self.density = DENSITY[self.symbol]

    
