import math
import csv
import pandas as pd


def zcount(data):
    return len(data)


def zmean(data):
    return round(sum(data) / zcount(data), 2)


def zmode(data):
    return round(max(set(data), key=data.count), 2)


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
    return round(math.sqrt(finale), 2)


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

    return round(math.sqrt(zvariance(data)), 2)


def zstderr(data):
    return round(zstddev(data) / math.sqrt(zcount(data)), 2)


def zcorr(datax, datay):
    return round(cov(datax, datay) / (zstddev(datax) * zstddev(datay)), 2)


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
    return round(covariance, 2)


def read_data_setx(file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        iterating = next(reader)
        listx = []
        for row in reader:
            listx.append(row[0])
    return [float(x) for x in listx]


def read_data_sets_y(file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        iterating = next(reader)
        listy = []
        for row in reader:
            listy.append(row[1])
    return [float(y) for y in listy]


def statistic_calculator(file):
    y_dataset = read_data_sets_y(file)
    print(y_dataset)
    x_dataset = read_data_setx(file)
    print(x_dataset)
    print(f'Count of items in x data set: {zcount(x_dataset)}\n',
          f'Count of items in y data set: {zcount(y_dataset)}\n',
          f'Mean of x data set: {zmean(x_dataset)}\n',
          f'Mean of y data set: {zmean(y_dataset)}\n',
          f'Sample Variance of x data set: {zvariance(x_dataset)}\n',
          f'Sample Variance of y data set: {zvariance(y_dataset)}\n',
          f'Median of x data set: {zmedian(x_dataset)}\n',
          f'Median of y data set: {zmedian(y_dataset)}\n',
          f'Mode of x data set: {zmode(x_dataset)}\n',
          f'Mode of y data set: {zmode(y_dataset)}\n',
          f'Sample std deviation x data set: {zstddev(x_dataset)}\n',
          f'Sample std deviation y data set: {zstddev(y_dataset)}\n',
          f'Standard error of the mean of x data set: {zstderr(x_dataset)}\n',
          f'Standard error of the mean of y data set: {zstderr(y_dataset)}\n',
          f'Correlation between x and y: {zcorr(x_dataset, y_dataset)}\n')

# print(statistic_calculator('dataOne.csv'))
# print(statistic_calculator('dataTwo.csv'))
# print(statistic_calculator('dataZero.csv'))
# print(statistic_calculator('dataThree.csv'))
