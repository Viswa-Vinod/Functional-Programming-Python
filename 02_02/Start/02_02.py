import math

def double(x):
    return 2 * x

def minus_one(x):
    return x - 1

def squared(x):
    return x * x

my_number = 3

function_list = [ double, minus_one, squared, math.sqrt ]
# my_number = squared(minus_one(double(my_number)))
# print(my_number)

for fn in function_list:
    my_number = fn(my_number)

print(my_number)
