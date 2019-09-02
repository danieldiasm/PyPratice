class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

## They work like regular functions but belong to the class’s 
# (and every instance’s) namespace.
    @staticmethod
    def staticmethod():
        return 'static method called'

myObject = MyClass()
myVar = myObject.method()
myVar0 = (myObject.method())[0]

myVar1 = MyClass.classmethod()
myVar2 = (MyClass.classmethod())[0]

myVar3 = myObject.classmethod()
myVar4 = (myObject.classmethod())[0]

print("1-------")
print(myVar)
print(myVar0)
print("2-------")
print(myVar1)
print(myVar2)
print("3-------")
print(myVar3)
print(myVar4)
