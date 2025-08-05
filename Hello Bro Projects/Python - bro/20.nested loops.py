rows = int(input("Enter the 3 of raws: "))
columns = int(input("Enter the # of columns: "))
sumbol = input("Enter a symbol to use:")

for x in range(rows): 
    for y in range(columns):
        print(sumbol, end="")
    print()