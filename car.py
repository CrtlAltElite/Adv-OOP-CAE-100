class Car():
    def __init__(self, make, model, color, year):
        self.make = make.upper()
        self.model = model.upper()
        self.color = color.upper()
        self.year = year

    #Human readable ver
    def __str__(self):
        return f"<Car | {self.year} {self.model}>"

    #Computer readable ver
    def __repr__(self):
        return f"<Car | {self.year} {self.make} {self.model} in {self.color}>"
    
    def  __eq__(self, __o):
        return self.year == __o.year

    def __lt__(self, __o):
        return  self.year < __o.year

    def __gt__(self, __o):
        return self.year > __o.year

    def __le__(self, __o):
        return self.year <= __o.year

    def __ge__(self, __o): 
        return self.year >= __o.year


delorean = Car('delorean', 'dmc-12', 'gray', 1981) # Back to the future
vw = Car('Volkswagon', 'Beetle', 'white', 1963) #Herbie
ford = Car('Ford', 'Econoline', 'fluffy', 1984) #dumb and dumber
lotus = Car('Lotus', "espirit", "gray", 1982) # the spy who loved me
pontiac = Car('Pontiac','Firebird', 'black', 1982) #knightrider

cars = [delorean, vw, ford, lotus, pontiac]
cars.sort()
print(cars)

print("Guess the film by car:")
for index, car in enumerate(cars):
    print(index+1, car)
