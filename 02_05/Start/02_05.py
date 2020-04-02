def create_printer():
    my_fav_number = 42
    def printer():
        print(f"my fav number is: {my_fav_number}")
    return printer

my_printer = create_printer()
my_printer()

def create_counter():
    count = 0
    def get_count():
        return count
    
    def increment_count():
        nonlocal count
        count = count + 1
    
    return (get_count, increment_count)

get_count, increment_count = create_counter()

increment_count()
increment_count()
increment_count()
print(get_count())
