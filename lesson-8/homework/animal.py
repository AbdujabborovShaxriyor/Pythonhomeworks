from abc import ABC, abstractmethod

#Base class

class Animal:
    @abstractmethod
    def __init__(self,name,type,color,sound):
        self.name=name
        self.type = type
        self.color = color
        self.sound = sound
    @abstractmethod
    def make_sound(self):
        print(f"{self.name} says {self.sound}")
        
#Dog class        
        
class Dog(Animal):
    def __init__(self, name, type, color, sound):
        super().__init__(name, type, color, sound)
    def make_sound(self):
        return super().make_sound()
    
#Cat class    
    
class Cat(Animal):
    def __init__(self, name, type, color, sound):
        super().__init__(name, type, color, sound)
    def make_sound(self):
        return super().make_sound()
    
