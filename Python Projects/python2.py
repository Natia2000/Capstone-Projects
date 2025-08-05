def get_number(number):
    while True:
        operand = input("Number " + str(number) + ": ") 
        try:
            return float(operand)
        except:
            print("Invalid number, try again.")

operand = get_number(1)
operand2 = get_number(2)
sign = input("Sign: ")
# while True:
#     operand = input("Number 1: ")
#     try:
#         operand = float(operand)
#         break
#     except:
#         print("Invalid numbert, try again.")


# while True:
#     operand2 = input("Number 2: ")
#     try:
#         operand2 = float(operand2)
#         break
#     except:
#         print("Invalid number, try again.")

result = 0
if sign == "+":
        result = (operand) + (operand2)
elif sign == "-":
        result = (operand) - (operand2)
elif sign == "/":
    if (operand2) != 0:
            result = (operand) / (operand2)
    else:
            print("Division by zero.")
        
elif sign == "*":
    result = (operand) * (operand2)
else:
    print("Invalid sign.")
print(result)
