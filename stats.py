from main import *


def mean(data):
    """
    Takes the a predefined list as an object and calculates its mean.
    """
    return sum(data) / len(data)


def variance(data):
    """
    Calculates the variance of a data set.
    """
    mu = mean(data)
    eps = []
    for i in data:
        eps.append((i - mu) ** 2)
    eps
    s = sum(eps)

    return s / len(data)


def stddev(data):
    """
    Calculates the standard deviation (or the square root of the variance) of the data set.
    """
    return sqrt(variance(data))


def median(data):
    data = sorted(data)
    l = len(data)
    if l % 2 != 0:
        return (len(data) + 1) / 2
    else:
        return (len(data) / 2 + (len(data) / 2 + 1)) / 2

def mode(data): 
    for i in data: 
        

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(median(data))
