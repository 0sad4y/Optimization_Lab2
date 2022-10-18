class Functions:
    h = 0.01

    def __init__(self, num: int):
        self.function_number = num

    def func(self, x: list):
        result = None
        if self.function_number == 1:
            result = 4 * (x[0] - 5) ** 2 + (x[1] - 6) ** 2
        elif self.function_number == 2:
            result = (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2
        elif self.function_number == 3:
            result = 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2 + 90 * (x[3] - x[2] ** 2) ** 2 + (1 - x[2]) ** 2 + \
                     + 10.1 * ((x[1] - 1) ** 2 + (x[3] - 1) ** 2) + 19.8 * (x[1] - 1) * (x[3] - 1)
        elif self.function_number == 4:
            result = (x[0] + 10 * x[1]) ** 2 + 5 * (x[2] - x[3]) ** 2 + (x[1] - 2 * x[2]) ** 4 + \
                     + 10 * (x[0] - x[3]) ** 4
        result = round(result, 6)
        return result

    def dif1(self, x: list, var_num: int):
        arguments = x.copy()
        arguments[var_num - 1] += self.h
        a = self.func(arguments)
        arguments[var_num - 1] -= self.h * 2
        b = self.func(arguments)
        result = (a - b) / (2 * self.h)
        result = round(result, 4)
        return result

    def dif2(self, x: list, first_var_num: int, second_var_num: int):
        arguments = x.copy()
        arguments[first_var_num - 1] += self.h
        a = self.dif1(arguments, second_var_num)
        arguments[first_var_num - 1] -= self.h * 2
        b = self.dif1(arguments, second_var_num)
        result = (a - b) / (2 * self.h)
        result = round(result, 4)
        return result
