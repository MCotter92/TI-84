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
    """
    Finds the middle number in the ordered list. If  no middle number exists because of the length of the list, it finds the mean of the middle two numbers.
    """
    data = sorted(data)
    l = len(data)
    if l % 2 != 0:
        return (len(data) + 1) / 2
    else:
        return (len(data) / 2 + (len(data) / 2 + 1)) / 2


def mode(data):
    """
    Finds the datapoint that occurs the most. Returns a touple that shows tells you the number that occurs the most and how many times it occurs. If
    """
    max_count = (0, 0)
    for i in data:
        occurences = data.count(i)
        if occurences > max_count[0]:
            max_count = (occurences, i)

    if max_count[1] == 1:
        return None
    else:
        return max_count


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mode(data))
