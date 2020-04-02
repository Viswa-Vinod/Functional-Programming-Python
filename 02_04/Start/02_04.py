def create_multiplier(num1):
    def multiplier(num2):
        return num2 * num1

    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(5))
print(triple(6))
# def createPrinter():
#     def printer():
#         print("hello function")

#     return printer

# my_printer = createPrinter()

# my_printer()
