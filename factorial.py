def factorial(x):
    """Thins finds the factorial of a number"""
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial.__doc__)
print("THE FACTORIAL OF 0 IS".lower(), factorial(0))
print("THE FACTORIAL OF 4 IS".lower(), factorial(4))
print("THE FACTORIAL OF 52 IS".lower(), factorial(52))