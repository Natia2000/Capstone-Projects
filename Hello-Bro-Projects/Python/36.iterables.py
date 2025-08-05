numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

for number in reversed(numbers):
    print(number, end="-")
    
    
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in (fruits):
    print(fruit)
    

name = "Bro Code"

for character in name:
    print(character, end=" ")
    
    
my_dictioinary = {"A": 1, "B": 2, "C": 3}

for value in my_dictioinary.values():
    print(value)
    
for key, value in my_dictioinary.items():
    print(f"{key} = {value}")