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


def mul(a: list, b: (float, list)):
    result = []

    if type(b) == float:
        for i in range(len(a)):
            result.append(a[i].copy())

        for row in range(len(a)):
            for col in range(len(a)):
                result[row][col] *= b
    else:
        for i in range(len(a)):
            temp = 0
            for j in range(len(a)):
                temp += a[i][j] * b[j]
            result.append(temp)

    return result


def det(a: list):
    result = 0

    if len(a) == 2:
        result = a[0][0] * a[1][1] - a[0][1] * a[1][0]
        return result

    for col in range(len(a)):
        temp_a = []
        for i in range(1, len(a)):
            temp_a.append(a[i].copy())

        for i in range(len(temp_a)):
            temp_a[i] = temp_a[i][0:col] + temp_a[i][col + 1:]

        sign = (-1) ** (col % 2)
        sub_det = det(temp_a)
        result += sign * a[0][col] * sub_det

    return result


def minor_matrix(a: list):
    result = []

    if len(a) == 2:
        result.append([a[1][1], a[1][0]])
        result.append([a[0][1], a[0][0]])
        return result

    for row in range(len(a)):
        result.append([])
        for col in range(len(a)):
            temp_a = []
            for i in range(len(a)):
                if i != row:
                    temp_a.append(a[i].copy())

            for i in range(len(temp_a)):
                temp_a[i] = temp_a[i][0:col] + temp_a[i][col + 1:]

            result[row].append(det(temp_a))

    return result


def inverse_matrix(a: list):
    length = len(a)
    minor_a = minor_matrix(a)
    d = det(a)
    if d == 0:
        return []

    for row in range(length):
        sign_row = (-1) ** (row % 2)
        for col in range(length):
            sign_col = (-1) ** (col % 2)
            minor_a[row][col] *= sign_col * sign_row

    alg_a = []
    for row in range(length):
        alg_a.append([])
        for col in range(length):
            alg_a[row].append(minor_a[col][row])

    result = mul(alg_a, (1 / d))

    return result
