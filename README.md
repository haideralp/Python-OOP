# Python OOP
 
## Step 1 - Example of Abstraction (Animal Class - Parent Class )

```python
class Animal:

    # __init to declare class attributies
    def __init__(self): #self refers current class
        self.alive = True
        self.spine = True

    def sleep(self):
        return "8 hours sleep is advised.."
    def eat(self):
        return  "eat healthy to stay fit"

# create an object of the class before using it
cat = Animal()

print(cat.eat()) # we abstracted how was eat created or what info is available.
```

### Step 2 - Example of Inheritance (Reptile - Inheriting from Animal.py)

```python

from animal import Animal

# create a reptile class
class Reptile(Animal): #write the name of the class in (parent-class) to inherit
    # parent class - base class - super class

    def    __init__(self):
        # to let it know to inherit everything from parent class
         super().__init__() # super is used to inherit everything from parent calss
         self.cold_blooded = True
         self.heart_chambers = [3,4]

    def seek_heat(self):
        return "it's a sunshine kind of day"

    def hunt(self):
        return "working hard to catch a next meal"

# create object of reptile class
reptile_object = Reptile()

#print(reptile_object.eat())
#print(reptile_object.hunt())
```