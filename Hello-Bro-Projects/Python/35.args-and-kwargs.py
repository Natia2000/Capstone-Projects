# def add(a, b):
#     return a + b

# print(add(1, 2))

# def add(*args):    #you can pass any number of arguments
#     total = 0             # you can change name args with any name
#     for arg in args:   
#        total += arg
#     return total


# print(add(1, 2, 3, 4, 5))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Spongebob", "Harold", "Squarepants")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 Fake St.", 
#               apt="100",
#               city="Detroit", 
#               state="MI",
#               zip="54321")
    

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")
        
shipping_label("Dr.", "Spongebob", "Squarepants", 
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit", 
               state="MI",
               zip="54321")