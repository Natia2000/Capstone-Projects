fruits = ["apple", "orange", "banana", "coconut"]
print(dir(fruits))
print(help(fruits))
print(len(fruits))  # length of collections
print("apple" in fruits)

fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("apple"))  
print(fruits.index("coconut"))

for fruit in fruits:
    print(fruit)





