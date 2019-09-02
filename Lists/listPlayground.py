## Not part of the course, but a thing that I wanted to test.

myListNo1 = [10,23,45]
myListNo2 = [33,65,75]
myListNo3 = ["Socks","T-Shirts","Pants"]

myMotherDict = {"List 1":myListNo1,"List 2":myListNo2,"List 3":myListNo3}

for key, value in myMotherDict.items():
    print("On list ",key," I have ",value)

items = [{'name':'soap','price':1.25},{'name':'banana','price':3.00},{'name':'plunger','price':7.50}]

def stock_price():
    # Add together all item prices in self.items and return the total.
    #allValues = [value['price'] for value in items]
    return sum([value['price'] for value in items])

print(stock_price())