#Functions and variables

#Method1
def cheese_and_crackers(cheese_count,crackers_count):
    print(f"A person has {cheese_count} cheeses !")
    print(f"But you end up having {crackers_count} crackers !")
    print(f"I think that should be enough for a party")
    print(f"Get a Blanket..\n..")

#By this way you call the functions and the value assignment operators
cheese_and_crackers(20,30)

#Method2
#Another method is by using different variables
print("We can do something else as well")
cheese=10
crackers=20

#Then call the function name with the new variables created

cheese_and_crackers(cheese,crackers)


#Method3
#Third method is to do by  using some basic math

print("We can use some math where we add 2+1 and 3+2:")
cheese_and_crackers(2+1,3+2)



#Method4
#The fourth method would be to apply operators
print("and we can combine two variables with some math:")
cheese_and_crackers(cheese+90,crackers+100)
