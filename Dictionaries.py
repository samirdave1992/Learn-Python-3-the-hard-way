person={'name':'Noma','Age': 37,'height':5*12+5 }

print(person['name'])

print(person['Age'])

person['city']="DFW"

print(person['city'])

print(person)


##Lets do some dictionaries for states

states={
    'Oregon':'OR',
    'Florida':'FL',
    'Texas':'TX',
    'California':'CA',
    'New York':'NY'
}

#Cities
cities={
    'CA':'San Francisco',
    'TX':'Dallas',
    'OR':'Portland'
}

#adding some cities
cities['NY']='New York'
cities['FL']='Florida'


print('--' * 10)

print("TX State had: ", cities['TX'])
print("OR State had: ", cities['OR'])


print("Florida state is abbrevated as : ", states['Florida'])
print("New York state is abbrevated as : ", states['New York'])



#Print using loops

print('--' * 10)
for states,abbrev in list(states.items()):
    print(f"State {states} is abbrevated as {abbrev}")




for abbrev,cities in list(cities.items()):
    print(f"{abbrev} has the city {cities}")



print('--' * 10)


for states,abbrev in list(states.items()):
    print(f"state {states}  is  as {abbrev}")
    print(f"and has city {cities[abbrev]}")

