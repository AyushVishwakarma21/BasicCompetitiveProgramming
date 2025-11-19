# a function is a block of reusable code /statements that return a specific 
# task it executes whenever it is called.

# example:

# def Hello():
#    print("Hello")

# Hello()


def make_tea():
    print("Tea is Here")

make_tea()


def hello(name):
    print("Greetings,",name)

hello("Ayush")

'''
parameter are the variable listed inside the parentheses in function.
arguments are the values that are passed to the function when it is called.

Q. write a function to print square of a number.
Q. wap to print the square of number from x to y.
Q. wap to implement pythagoras theorem using function.
Q. wap to make the calculator using function.
'''

def square(num):
    print("Square:",num**2)

def square_nums(num1,num2):
    for i in range(num1,num2+1):
        print("Squares:",i**2,end=" ")

square(4)
square_nums(1,5)

def pythagoras(a,b):
    print("Third is:",((a**2)+(b**2))**0.5)

pythagoras(2,3)
