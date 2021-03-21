ten_things= 'Apples Oranges Bananas Grapes Grapefruit'

stuff=ten_things.split()

more_stuff=["Papaya", "Honey","Peach","Strawberry","Figs","Clementines"]

while len(stuff) != 10:
    next_one=more_stuff.pop()
    print("adding", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")


print("There you go:", stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print('   '.join(stuff))
print('#'.join(stuff[3:5]))


print(more_stuff)


#For loop in lists

Bikes=['Honda','Yamaha','Suzuki','Ducati']

for items in Bikes:
    print (f"{items} is a great bike")


#Numerical lists
for anything in range(1,9):
    print(anything)



#populating a empty list

to_be_full=[]
for value in range(0,15):
    fibo=value+3
    to_be_full.append(fibo)
print(to_be_full)
