import math


def zcount(data):
    return len(data)


def zmean(data):
    return sum(data) / zcount(data)


def zmode(data):
    return max(set(data), key=data.count)


def zmedian(data):
    sorted_list = sorted(data)
    if zcount(data) % 2 == 0:
        return sorted_list[(math.ceil(len(sorted_list) / 2))]
    else:
        return (sorted_list[math.ceil(len(sorted_list) / 2)] + sorted_list[math.floor(len(sorted_list) / 2)]) / 2


def zvariance(data):
    sum_of = sum(data)  # step 1
    squared_and_divided = (sum_of * sum_of) / zcount(data)  # step 2
    each_squared = []
    for i in data:  # step 3
        each_squared.append(i ** 2)
    sum_of_squared = sum(each_squared)  # step 3
    difference = sum_of_squared - squared_and_divided  # step 4
    one_less = zcount(data) - 1  # step 5
    finale = difference / one_less  # step 6
    return math.sqrt(finale)


def zstddev(data):
    # calculated_mean = zmean(data)
    # subtract_from_mean = []
    # for i in data:
    #     subtract_from_mean.append(i - calculated_mean)
    # squared_deviation = []
    # for i in subtract_from_mean:
    #     squared_deviation.append(i * i)
    # population_vari = (sum(squared_deviation)) / (zcount(data))
    # return math.sqrt(population_vari)

    return math.sqrt(zvariance(data))

def zstderr(data):
    return zstddev(data) / math.sqrt(zcount(data))

def zcorr(datax, datay):
    return zcorr(datax, datay)/(zstddev(datax)*zstddev(datay))


def cov(datax, datay):
    meanx = zmean(datax)
    meany = zmean(datay)
    subtract_from_meanx = []
    for i in datax:
        subtract_from_meanx.append(i - meanx)
    subtract_from_meany = []
    for i in datay:
        subtract_from_meany.append(i - meany)
    multiplied = list(map(lambda x, y: x * y, subtract_from_meany, subtract_from_meanx))
    sum_of_multiplication = sum(multiplied)
    covariance = sum_of_multiplication / zcount(multiplied)
    return covariance

