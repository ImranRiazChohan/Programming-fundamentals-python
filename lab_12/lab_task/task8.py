import random 
lst1=[1,2,3,4,6,7,43]

#choice()
print("A random number from list is :",end="")
print(random.choice(lst1))

#randrange()
print("A random number from range is :",end="")
print(random.randrange(10,40,5))

#random()
print("A random number between 0 an 1 is :",end="")
print(random.random())

#seed()
random.seed(4)
print("the mapped random number with 4 is :",end="")
print(random.random())
print("the list before shuffling is :",end="")
for i in range(0,len(lst1)):
    print(lst1[i],end=" ")
print("\r")

#shuffle()
random.shuffle(lst1)
print("the list after shuffling is :",end="")
for i in range(0,len(lst1)):
    print(lst1[i],end=" ")
print("\r")    

#uniform()
print("the random floating point numbe between 5 and 10 is :",end="")
print(random.uniform(5,10))