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


