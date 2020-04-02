def say_hello_1(name):
    print(f"hello {name}")

say_hello_2 = say_hello_1
say_hello_2("Vinod")

ENVIRONMENT = "DEV"

def fetch_data_real():
    print("Doing some time intensive ops")
def fetch_data_fake():
    print("returning fake data")
    return {
        "name": "Vinod",
        "age": "35"
    }

fetch_data = fetch_data_real if ENVIRONMENT == "PROD" else fetch_data_fake

data = print(fetch_data())
