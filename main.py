import functions
import matrix
from minimum import find_minimum
import alpha


def main():
    function_index = 1
    method_index = 3
    accuracy = 0.001
    x = [0, 0]
    h = [1, 1]
    grad = []
    f = functions.Functions(function_index)

    if method_index == 1:
        pass
    elif method_index == 2:
        while True:
            grad = matrix.gradient(f, x)

            if matrix.norm(grad) < accuracy:
                break

            a = alpha.Alpha(f, x, grad, False)
            a_min = find_minimum(a)

            for i in range(len(x)):
                x[i] -= a_min * grad[i]

        result = x
    elif method_index == 3:
        while True:
            grad = matrix.gradient(f, x)

            if matrix.norm(grad) < accuracy:
                break

            h = matrix.gesse_matrix(f, x)
            h = matrix.inverse_matrix(h)
            p = matrix.mul(matrix.mul(h, -1.0), grad)

            a = alpha.Alpha(f, x, p, True)
            a_min = find_minimum(a)

            for i in range(len(x)):
                x[i] += a_min * p[i]

        result = x

    print(result)


if __name__ == '__main__':
    main()
