# dictionary

grades = {"Sandy": "A", "Squidward": "B", "Spongebob": "C", "Patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")


email = "BroCode@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")