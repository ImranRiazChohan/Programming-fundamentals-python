# Parent class
class Dog:

    # Class attribute
    species = 'mammal'
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    # Child class (inherits from Dog() class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    # Child class (inherits from Dog() class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    # Child classes inherit attributes and
    # behaviors from the parent class
thunder = Bulldog("Thunder", 9)
print(thunder.description())
# Child classes have specific attributes
# and behaviors as well
print(thunder.run("slowly"))
# Is thunder an instance of Dog()?
print(isinstance(thunder, Dog))
#Is thunder_kid an instance of Dog()?
thunder_kid = Dog("ThunderKid", 2)
print(isinstance(thunder, Dog))
# Is Kate an instance of Bulldog()
Kate = RussellTerrier("Kate", 4)
print(isinstance(Kate, Dog))
# Is thunder_kid and instance of kate?
print(isinstance(thunder_kid, Dog))
print("Thanks for understanding the concept of OOPs")