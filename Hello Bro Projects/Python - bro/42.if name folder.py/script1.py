
# print(dir())

# print(__name__)

# from script2 import *
# print(__name__)

def favorite_food(food):
    print(f"Your favorite food is{food}")
    
def main():
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")
    
if __name__ == "__name__":
    main()
    
