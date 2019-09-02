#Unpacking args with *
#Daniel Z. Dias de Moraes - Sep 2019
def multiArgs(*args):
    print(args)
    total = 0
    for arg in args:
        total += arg
    print(total)

def argReceiver(*canBeAnything):
    #Note that args always comes as a tuple!
    print(canBeAnything)

# Calling those methods
multiArgs(1,2,3,4)
argReceiver("This is a test")

# Now let's checkout using a list to feed an input

def add(x,y):
    return x + y

numsList = [3,5]
numsDict = {"y":25, "x":15}

# This won't work because only the first number will be received, missing
# the second parameter
# added1 = add(numsList)

# FEEDING WITH A LIST
# In this case * will feed the funct add with numbers on its order.
# THE LIST MUST HAVE ONLY TWO NUMBERS INSIDE, obviously, otherwise it
# will have too many or too few parameters.
added2 = add(*numsList)
print(added2)

# FEEDING WITH A DICTIONARY
# This is the cooler way to feed a funct, because it uses key-value pairs.
# Seeking by it own for the key that matches the arg name.
# but ALSO MUST HAVE ONLY TWO PAIRS INSIDE!
added3 = add(**numsDict)
print(added3)

# And without notice you've learned args and kargs...(Args and Key-Value Args)
# Hope it could be a reference to someone.