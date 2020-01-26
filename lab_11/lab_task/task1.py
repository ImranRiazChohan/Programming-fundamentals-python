class Dog:
    # Class Attribute
    species = 'mammal'
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)
    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
# Instantiate the Dog object
razer = Dog("Razer", 6)
# call our instance methods
print(razer.description())
print(razer.speak("Woof Woof"))