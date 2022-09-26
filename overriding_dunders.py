from datetime import datetime as dt

class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.created_on = dt.utcnow()
        print(self.first_name, "is Alive!!!!")
        
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        """Human readable output -- should be unique"""
        return f"<Person | {self.full_name}>"
    
    def __repr__(self):
        """Machine Readable Output -- should be unique"""
        return f"<Person | {self.last_name} {self.created_on.strftime('%c')}>"

    def __hash__(self):
        return hash(self.full_name+self.created_on.strftime("%c"))

    def __bool__(self):
        return self.age > 0
    
    def __del__(self):
        print(f"Our person {self.full_name} has died")

    def  __eq__(self, __o):
        return self.age == __o.age

    def __lt__(self, __o):
        return  self.age < __o.age

    def __gt__(self, __o):
        return self.age > __o.age

    def __le__(self, __o):
        return self.age <= __o.age

    def __ge__(self, __o): 
        return self.age >= __o.age

    


matt = Person(first_name="Matt", last_name ="Leblanc", age = 53)
lisa = Person(first_name="Lisa", last_name ="Kudrow", age = 55)
steve = Person(first_name="Steve", last_name ="Nash", age = 55)
bambam = Person(first_name="Bambam", last_name="Rubble", age=0)

print(matt)
print(repr(matt))
print(hash(matt))
print(matt==lisa)
print(lisa==steve)

print("="*20)
print(lisa == steve) # True
print(lisa > steve) # False
print(lisa < steve) # False
print(lisa >= steve) # True
print(lisa <= steve) # True
print("="*20)
print(lisa == matt) #False
print(matt > lisa)  #False
print(matt < lisa) #True
print(matt >= lisa) # False
print(matt <= lisa) # True
# if matt:
#     print("matt is alive")
# else:
#     print("Matt has not be born yet")

# if bambam:
#     print("bambam is alive")
# else:
#     print("bambam has not be born yet")

# people = [matt, lisa, steve, bambam]
# for person in people:
#     if person:
#         print(f"{person.full_name} is alive")
#     else:
#         print(f"{person.full_name} has not be born yet")

people = [matt, lisa, steve, bambam]
print(people)
print(sorted(people))
print(sorted(people, reverse=True))


# make a Class of Car that that will be sorted by its year