"""arithmetic operation"""

def add(a, b):
    return (a + b)

def sub(a, b):
    return (abs(a - b))

def mul(a, b):
    return (a * b)

def div(a, b):
    try:
        return (a / b)
    except ZeroDivisionError:
        return ("not possible because divider is 0")
