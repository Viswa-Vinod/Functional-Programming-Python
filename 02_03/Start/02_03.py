def add(x,y):
    return x + y

def subtract(x,y):
    return x - y


def combine_2_and_3(fn):
    return fn(2,3)

print(combine_2_and_3(min))

def combine_name(fn):
    return fn("Vinod", "Kumar")

def fullName(fname, lname):
    return f"{fname} {lname}"

print(combine_name(fullName))

def reverseName(fname, lname):
    return f"{lname}, {fname}"

print(combine_name(reverseName))
