# a decorator is a function that modifies or enhance another function without changing the original code.
# uses
# 1. tO reuse code
# 2. pass it as an arg.
# 3. to keep the code clean
# 4. to enhance readability and maintainability

# basic syntax

def decorator (func):
    def wrapper (*args, **kwargs):
        # code to be executed before calling the original function
        print("Before calling the function")

        func(*args, **kwargs)

        # code to be executed after calling the original function
        print("After calling the function")

        # return result
    return wrapper

@decorator
def greet(name):
    print(f'Hello, {name}!')

greet("Hamida")

