#Inheritance
class animal:
    def sound(self):
        return "generic sound"
class Dog(animal):
    def sound(self):
        return "woof"
my_dog = Dog()
generic_sound = my_dog.sound()
print(generic_sound)

