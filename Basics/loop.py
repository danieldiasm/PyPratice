## Automated Testing with Python

my_variable = "Hallo"
#A string is an iterable, like lists, sets, tuples and more.

#print(my_variable[0])

for char in my_variable:
    print(char)


my_list = [1, 2, 3, 4, 55, 66, 77]

for number in my_list:
    print(number)


user_wants_numbers = True
i = 0
while user_wants_numbers == True:
    print(10)
    i += 1

    if (i > 10):
        print("this crap has now 10!")
        break
    elif (i < 10):
        print("Penis")