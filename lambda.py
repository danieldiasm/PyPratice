#Pratice file and notes over a simple Lambda Function
#Daniel Z. Dias de Moraes - Sep 2019

# How does a lambda fucntion looks like:
# (lambda param1, param2: param1 "action" param2)(val_for_p1, val_for_p2)
# Now, a sample:
sampleVar = (lambda x, y: x + y)(1,2)

print(sampleVar)


#Now something a bit more complex...

numberList = [1,2,3,4,5,6,7,8,9,10]

# This works on list comprehention
doubledList = [(lambda x: x * 2)(x) for x in numberList]

# We can break it into, lambda keypoint (lambda x: x * 2)(x)
# basically it gets each iteration of L.C. and output the value doubled.

#We can also use map, but list conversion is necessary, otherwise it will return an object.
doubledListTwo  = list(map(lambda x: x*2, numberList))

#Finally, print
print(numberList)
print(doubledList)
print(doubledListTwo)