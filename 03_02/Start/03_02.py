numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def double(x):
    return x * 2
def isGreaterThan2(x):
    return x > 2

print([double(x) for x in numbers_list])
print(list(filter(isGreaterThan2, numbers_list)))
print([x for x in numbers_list if x > 3])

add = lambda x, y: x + y
print(add(3,4))
