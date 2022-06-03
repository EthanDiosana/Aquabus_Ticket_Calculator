class Pass_Container():
    """Holds all of the passes. Has some useful functions."""

    Passes={}

    def addPass(self, pass_to_add):
        """Adds a pass to the Passes{} dictionary."""
        self.Passes[pass_to_add.name] = pass_to_add

    def passIsInContainer(self, pass_name):
        """Returns true if the given pass name is in the Passes{} dictionary. Returns false otherwise."""
        if(pass_name in self.Passes):
            return False
        else:
            return True

    def printAllPasses(self):
        for item in self.Passes.keys():
            print(self.Passes[item].toString())
