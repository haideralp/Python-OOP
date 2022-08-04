# create an Animal Class
# syntax class Name:

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

#print(cat.eat()) # we abstracted how was eat created or what info is available.