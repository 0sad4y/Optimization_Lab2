import alpha


def find_minimum(alp: alpha.Alpha):
    point = [1]
    step = 0.1
    a = 0
    b = 0
    k = 0
    accuracy = 0.001
    difference = accuracy / 10
    is_finished = False

    if alp.func(point[0]) > alp.func(point[0] + step):
        a = point[0]
        point.append(point[0] + step)
        k = 2
    else:
        if alp.func(point[0] - step) >= alp.func(point[0]):
            a = point[0] - step
            b = point[0] + step
            is_finished = True
        else:
            b = point[0]
            point.append(point[0] - step)
            step = -step
            k = 2

    while not is_finished:
        point.append(point[0] + 2 ** (k - 1) * step)

        if alp.func(point[k - 1]) > alp.func(point[k]):
            if step > 0:
                a = point[k - 2]
            else:
                b = point[k]
            k += 1
        else:
            if step > 0:
                b = point[k]
            else:
                a = point[k]
            is_finished = True

    while (b - a) / 2 >= accuracy:
        x1 = 0.5 * (a + b) - difference
        x2 = 0.5 * (a + b) + difference
        if alp.func(x1) <= alp.func(x2):
            b = x2
        else:
            a = x1

    result = (a + b) / 2

    return result
