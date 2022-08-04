# Inherit reptile from reptile

from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    # def use_tongue_to_smell(self):
        # return " I can use my tongue to smell"

    # Example of Protect Encapsulation
    # def _colour (self):
        # return "I am a black python-protected"

    # Example of Private Encapsulation
    # def __sound(self):
        # return "Hissing- I will privately encapstulate you"

    # Exception handling with try and except blocks
    def _colour(self):
        try: #if
            return snake_object._colour()
        except RecursionError: # elif - else
            return " this is information is protected or hidden"



snake_object = Snake()

# print(snake_object.eat()) # this function is inherited from Animal
# print(snake_object.seek_heat()) # this function is from the Reptile class
# print(snake_object.use_tongue_to_smell()) # this function is from the snake class
# print(snake_object._colour())
# print(snake_object.__sound())

# create two more functions one with _ the other one with __
# execute them both - return message should explain Encapsulation down - public, protected, private.


# what type of errors & exceptions have you seen so far
# syntax error
# indentation error - value error - attribute error


# Try
    # print()
    # return
    # except name_of_error:
        # print()
        # return
    # finally
        # print ("better luck next time")
""""
try:
    print("test")
except:

"""
