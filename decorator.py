def decorator(func):
    def inner():
        print("before the func is called")
        func()
        print("after the function is called")
    return inner

def decorator2(func):
    def inner():
        func()
        print("I did a bunch of cool stuff")

    return inner



@decorator2
@decorator
def my_func():
    print("This is inside the function")


my_func()
# decorator(my_func)()

####################################################################


def add_two(func):
    def inner(x,y):
        return func(x,y)+2
    return inner

@add_two
def my_func(x,y):
    return x+y

print(my_func(3,2))

# Function to be decorated should give me the first name of a person
# Its decorator should return the first name as a string with is awesome
#  attached if the name starts with a [m, d, k]
# if not not it should says that the name smells like teen spirit
# There needs to be also some driver code
names = ["Connor F", "Kevin R", "Dylan S", "Diana B", "Caleb S", "Lizette E", "Gulfem A", "Marcus B", "Marco V"]
# Connor smells like Teen Spirit
# Kevin is awesome
# Dylan is awesome
# Diana is awesome
# Caleb smells like Teen Spirit
# Lizette smells like Teen Spirit
# Gulfem smells like Teen Spirit
# Marcus is awesome
# Marco is awesome

def add_suffix(func):
    def inner(s):
        if func(s)[0].lower() in {"m","d","k"}:
            return func(s) + " is awesome"
        else:
            return func(s) + " smells like Teen Spirit"
    return inner

@add_suffix
def first_name(s):
    first = s.split()[0]
    return first


for name in names:
    print(first_name(name))