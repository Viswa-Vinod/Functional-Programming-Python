from functools import partial

def add(x, y, z):
    return x + y + z

def addPartial(x):
    def addOthers(y, z):
        return x + y + z
    return addOthers


add5 = addPartial(5)
print(add5(6,7))

def add_partial_2(x,y):
    def addOthers(z):
        return x + y + z
    return addOthers


add_5_and_6 = add_partial_2(5,6)

print(add_5_and_6(7))

def curry_add(x):
    def curry_add_inner(y):
        def curry_add_inner_2(z):
            return x + y + z
        return curry_add_inner_2
    return curry_add_inner

add5 = curry_add(5)
add_5_and_6 = add5(6)
add_5_and_6_and_7 = add_5_and_6(7)

print(add_5_and_6_and_7)
print(curry_add(5)(6)(7))

add_5 = partial(add, 5)
print(add_5(6,7))
