class FourLegs:
    def run(self):
        print("Running on 4 legs")

class Furry:
    def brush(self):
        print("brushing out the hair")

    def run(self):
        print("I have no legs!!!!")

    
class Dog(FourLegs, Furry):
    def __init__(self):
        super().__init__()

buster = Dog()
buster.run() # running on 4 legs
buster.brush()

class Dog(Furry, FourLegs):
    def __init__(self):
        super().__init__()

buster = Dog()
buster.run() # I have no legs!!!
buster.brush()


class Dog(Furry, FourLegs):
    def __init__(self):
        super().__init__()
    
    def run(self):
        print("Galloping")

buster = Dog()
buster.run() # I have no legs!!!
buster.brush()