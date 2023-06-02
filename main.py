def add(x, y):
    """
    Adds two objects together.
    """
    return x + y


def subtract(x, y):
    """
    Subtracts one object from another.
    """
    return x - y


def multiply(x, y):
    """
    Multiplies two objects together.
    """
    return x * y


def divide(x, y):
    """
    Divides x by y.
    """
    return x / y


def power(x, y):
    """
    Raises x to the power of y.
    """
    return x**y


def sqrt(x):
    """
    Finds the square root of x.
    """
    return x**0.5


def log(x, base):
    """
    A function that returns the log of a number given a provided base.
    """
    count = 0
    while base <= x:
        count += 1
        x /= base
    return count  # Need to find a better way to calculate logs of numbers and bases that don't have a whole number  output. Example: function gives log(144,11) = 2 instead of 2.075.


if __name__ == "__main__":
    print(log(144, 11))
