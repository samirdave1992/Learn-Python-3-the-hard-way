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
