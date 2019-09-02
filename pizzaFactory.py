# Python Class Methods - Pratice file of "Magic Methods"
# Daniel Z. Dias de Moraes, August 2019
import math

class Pizza:
    def __init__(self, flavor, ingredients, radius):
        self.flavor = flavor
        self.ingredients = ingredients
        self.radius = radius

    # This is an unambiguous representation of the object instance
    def __repr__(self):
        return (f'Flavor({self.flavor!r}), '
                f'Pizza({self.ingredients!r}), '
                f'({self.radius!r})')

    # This is a textual representation of the object instance
    def __str__(self):
        return f"A pizza {self.flavor} flavor, {self.ingredients} in it, and size {self.radius}."

    def area(self):
        return self.circle_area(self.radius)

## Class methods don’t need a class instance.
#  They can’t access the instance (self) but
#  they have access to the class itself via cls.
    @classmethod
    def margherita(cls):
        return cls('Margherita',['mozzarella','tomatoes','basil'], 15)
    
    @classmethod
    def prosciutto(cls):
        return cls('Prosciutto',['mozzarella','tomatoes','ham'], 15)

## Static methods don’t have access to cls or self.
#  They work like regular functions but belong to 
#  the class’s namespace.
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

# I've used it as a helper to instantiate a new Pizza flavor
# helping me to not write everything up again, just like a recipe.
myPizza = Pizza.margherita()

print("My pizza is a: ",myPizza.flavor)
print("It contains: ",[ingredient for ingredient in myPizza.ingredients])
print("It's size is:", myPizza.area(),"cm²")

print(myPizza.__repr__())

print(myPizza)