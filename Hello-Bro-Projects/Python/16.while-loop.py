name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")


# use not logical operator:
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit)")

print("bye")

num = int(input("Enter a # between 1 - 10: "))


# use or logical operator
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))
print(f"Your number is {num}")



