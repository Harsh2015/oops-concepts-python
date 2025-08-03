class Dog():
    def make_sound(self):
        print("Woof")
        
class Cat():
    def make_sound(self):
        print("Meow")
        
def animal_sound(animal):
    animal.make_sound() # calling same function (Behaviour) for different Animals
    
c = Cat()
d= Dog()
    
animal_sound(c)
animal_sound(d)
    
    
        
