class Pass():
    """Contains the information for a Pass."""

    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = float(price)

    def toString(self):
        return ("Name: %s\nType: %s\nPrice: %f\n"%(self.name, self.type, self.price))
