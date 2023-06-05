# calcmain1.py with a main function
from mycalculator import add as my_add
from mycalculator import substract as my_substract
from myrandom import random_2d, random_1d

def my_main():
    """This is a main function which generates two random numbers\
    and the apply calculator functions on them"""
    x = random_2d()
    y = random_1d()
    
    sum = my_add(x, y)
    diff = my_substract(x, y)
    
    print("x = {}, y = {}".format(x, y))
    print("sum is {}".format(sum))
    print("diff is {}".format(diff))

"""This is executed only if the special variable '__name__' is set as main"""
if __name__ == "__main__":
    my_main()

