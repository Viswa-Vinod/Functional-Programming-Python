def divide(x, y):
    return x / y

def second_argument_isnt_zero(fn):
    def safe_version(*args):
        if args[1] == 0:
            print("Warning second argument is 0")
            return
        return fn(*args)
    return safe_version

divide_safe = second_argument_isnt_zero(divide)

print(divide_safe(2,6))
