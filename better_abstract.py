from abc import ABC, abstractmethod
## Head First Design Patterns (OReilly) Eric Freeman

class Duck(ABC):
    @abstractmethod
    def display(self):
        pass

class Swimmable(ABC):
    
    def swim(self):
        print("floating on the pond")

class Quackable(ABC):
    
    def quack(self):
        print("Quack!")

class Flyable(ABC):
    
    def fly(self):
        print("flap flap flap")


class RedHead(Duck, Swimmable, Quackable, Flyable):
    def display(self):
        print("I am a red headed duck")

class Mallard(Duck, Swimmable, Quackable, Flyable):
    def display(self):
        print("I am a Mallard!")

class Rubberduck(Duck, Quackable, Swimmable):
    def display(self):
        print("I am a rubber ducky!")

    def quack(self):
        print("Squeeak")

class DecoyDuck(Duck, Swimmable):
    def display(self):
        print("I am a decoy")
    
