# lambda arguments : expression
def add_ten(a, func):
    return func(a)


x = add_ten(5, lambda a: a + 10)
print(x)  # 15


# multiple arguments
def run_two_digit_operation(num1, num2, func):
    return func(num1, num2)


y = run_two_digit_operation(5, 6, lambda a, b: a * b)
print(y)  # 30
