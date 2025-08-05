#  variable scope

def func1():
    a = 1
    print(a) # variable a is local to func1()

def func2():
    b = 2
    print(b)
    
func1()
func2()  # invoke the function


def func1():
    x = 1
    
    def func2():
        x = 2
        print(x)
    func2()  
                    #enclosed functon
func1()


# global scope, global version of x

def func1():
    print(x)
def func2():
    print(x)
x = 3

func1()
func2()



# global scope

from math import e
def func1():
    print(e)

e = 3
print(e)