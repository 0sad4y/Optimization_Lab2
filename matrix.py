import functions
from math import sqrt


def norm(x: list):
    result = 0
    for i in range(len(x)):
        result += x[i] ** 2
    result = sqrt(result)
    return result


def gradient(f: functions.Functions, x: list):
    result = []
    for i in range(1, len(x) + 1):
        result.append(f.dif1(x, i))
    return result


def gesse_matrix(f: functions.Functions, x: list):
    result = []
    for i in range(1, len(x) + 1):
        result.append([])
        for j in range(1, len(x) + 1):
            result[i - 1].append(f.dif2(x, i, j))
    return result
