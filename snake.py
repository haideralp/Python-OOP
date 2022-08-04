# Inherit reptile from reptile

from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return " I can use my tongue to smell"

snake_object = Snake()

print(snake_object.eat()) # this function is inherited from Animal
print(snake_object.seek_heat()) # this function is from the Reptile class
print(snake_object.use_tongue_to_smell()) # this function is from the snake class

# create two more functions one with _ the other one with __
# execute them both - return message should explain Encapsulation down - public, protected, private.

def

