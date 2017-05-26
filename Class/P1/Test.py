class NewClass():
    clasvariable = "remain constant for all instances until it is overwritten"
    
    def __init__(self, instname):
        self.instname = instname

class SecondClass():
    clasvariable = "2nd class's class variable"
    def __init__(self, name):
        self.name = name
