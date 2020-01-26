import random

#for choice()
print("choice: ",random.choice([1,2,3,4,5,6,7,8,9]))
#for randrange()
print("randrange: ",random.randrange(1,10))
#for randint()
print("randint:",random.randint(1,4))
#for random()
print("random: ",random.random())
#for shuffle()
lst=[2,5,31,421] 
random.shuffle(lst) 
print("shuffle: ",lst)
#for seed ()
random.seed(7)
print("seed: ",random.random())
#for uniform()
print("uniform: ",random.uniform(1,7))