## Set operations

set_one = {1, 3, 5, 7}
set_two = {1, 2, 3, 4, 6, 8}
set_three = {9, 10}

print("Intersection")
print(set_one.intersection(set_two))
print("Union")
print(set_one.union(set_two))
print(set_one.union(set_two, set_three))
print("Difference")
print(set_one.difference(set_two))