# Dictionary Comprehention
# Daniel Z. Dias de Moraes - Sep 2019

#There is a list
users = [
    (0, "Rob", "passwd"),
    (1, "Rolf", "1234"),
    (2, "Daniel", "hund4dog"),
    (3, "Jessica", "chirp2bird"),
]

#There is a list comprehension inputing values inside a dict
#In this format 'JohnDoe':(tuple), resulting dict = {'user':(0,"user","password")}
username_map = {user[1]:user for user in users}

username_input = input("Enter the USERNAME:")
password_input = input("Enter the PASSWORD:")

try:
    # Here we extract the data from a dict key-value pair, like so:
    #    user_id_number, username, password = username_map[key]
    # see, the three values comes from the tuple of the key-value pair, value.
    # The _ is used as blank variable (like in Go Lang).
    _, username, password = username_map[username_input]
    print("%s is a valid name!" % (username))
    print("The password is:", password)
except KeyError as ERROR1:
    print(f"{ERROR1} IS AN INVALID USERNAME!")

# print(username_map)
# print(list(username_map))