import collections
import math
import random

def standard_deviation(data):
    average = sum(data) // len(data)
    weighted_average = 0
    for value in data:
        weighted_average += ((value - average) ** 2)
    weighted_average //= len(data)
    return int(math.sqrt(weighted_average))

def median(data):
    data = sorted(data)
    midpoint = len(data) // 2
    if len(data) % 2 == 0:
        lower = data[midpoint-1]
        higher = data[midpoint]
        return (lower + higher) / 2
    else:
        return data[midpoint-1]

def pearson_skewness_coeff(mean, median, standard_dev):
    coeff = 3 * (mean - median)
    coeff //= standard_dev
    return coeff

if __name__ == '__main__':
    average_hb = collections.deque()
    for i in range(30):
        average_hb.append(random.randint(110,120))

    mean = sum(average_hb) / len(average_hb)
    _median = median(average_hb)
    standard_dev = standard_deviation(average_hb)
    print(pearson_skewness_coeff(mean, _median, standard_dev))

    off_hb = collections.deque()
    for j in range(30):
        off_hb.append(random.randint(100,140))

    mean = sum(off_hb) / len(off_hb)
    _median = median(off_hb)
    standard_dev = standard_deviation(off_hb)
    print(pearson_skewness_coeff(mean, _median, standard_dev))

    ireg_hb = collections.deque()
    for k in range(30):
        ireg_hb.append(random.randint(80,160))

    mean = sum(ireg_hb) / len(ireg_hb)
    _median = median(ireg_hb)
    standard_dev = standard_deviation(ireg_hb)
    print(pearson_skewness_coeff(mean, _median, standard_dev))
