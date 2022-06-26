def hello_decorator(func):
    def inner1(*args, **kwargs): # Note inner1 can be named whatever I want including wrapper etc.

        print("\nbefore Execution args: ", *args)

        print('keyargs --', list(kwargs.values()))
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution \n")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


@hello_decorator
def product_of_3(a, b, c):
    print("Inside the function")
    return a * b * c


_a, _b, _c = 1, 2, 3

# getting the value through return of the function
print("Sum =", sum_two_numbers(_a, _b))
print("Sum with key args =", sum_two_numbers(a=2, b=3))
print("Product with a positional arg & key arg =", product_of_3(_a, _b, c=5))


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_appa = return_greeting("Appa")

print(hi_appa)