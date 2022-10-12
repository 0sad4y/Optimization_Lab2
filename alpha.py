import functions


class Alpha:
    def __init__(self, f: functions.Functions, x: list, y: list, is_positive: bool, number=None):
        self.f = f
        self.x = []
        self.y = []
        self.is_positive = is_positive
        self.number = number
        for i in range(len(x)):
            self.x.append(x[i])
            self.y.append(y[i])

    def func(self, a: float):
        arguments = []
        if self.is_positive:
            sign = 1
        else:
            sign = -1

        for i in range(len(self.x)):
            arguments.append(self.x[i] + sign * a * self.y[i])

        result = self.f.func(arguments)

        return result
