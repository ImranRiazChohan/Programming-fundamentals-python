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
# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    # Child class (inherits from Dog class)
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
spinter = Bulldog("Spinter", 12)
print(spinter.description())
print(spinter.run("fast"))
roger = RussellTerrier("Roger", 5)
print(roger.description())
print(roger.run("quickly"))