def first(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")

def two(arg1, arg2):
    print(f"arg1:{arg1},arg2{arg2}")

def three(arg1):
    print(f"arg1:{arg1}")

def four():
    print("I got nothin'.")

first("Samir","Dave")
two("Samir","Dave")
three("Just one !")
four()



def greet_user():
    "This is a greeting"
    print("Hello")

greet_user()



##passing the info

def greet_user(username):
    print(f"Hello, {username}")

greet_user(input('Type your name: '))




def greet_pet(your_name,pet_name):
    print(f"Hello {your_name}")
    print(f"You have a wonderful pet {pet_name}")

greet_pet(input("Type your name:"),input("Type pet name:"))



def makepizza(*toppings):
    """This is needed to make a Pizza"""
    print(toppings)

makepizza('Pepperoni','Tomato','Cheese')



#Or
def makepizza(*toppings):
    """This is needed to make a Pizza"""
    print("This is needed to make Pizza:")

    for topping in toppings:
        print(f"-{topping}")

makepizza('Pepperoni','Tomato','Cheese')

