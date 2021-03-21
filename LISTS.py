Bikes=['Honda','Yamaha','Suzuki','Ducati']

print(Bikes)

#Print a specific element using numbers

print(Bikes[2])
print(Bikes[-2])

#Extracting values to print from the list

message=f"My first bike was {Bikes[2].title()}"
print(message)


##Adding , removing elements from the list

Bikes[0]='Harley'

print(Bikes)

#Append -Adding the element at the end of the list

Bikes.append('Triumph')
print(Bikes)

#Use insert to specify element position
Bikes.insert(0,'KTM')
print(Bikes)

#remove the motorcycle
Popped_value=Bikes.pop()

print(Popped_value)
print(f"The value that was Popped was {Popped_value}")


#Use positional values
first_value=Bikes.pop(1)

print(f"The second value that was popped is {first_value}")


#Removing the value
print(Bikes)
Bikes.remove('KTM')
print(Bikes)


#Organizing the list

Bikes.sort()
print(Bikes)

Bikes.sort(reverse=True)

print(Bikes)


