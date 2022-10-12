import functions
import matrix
from minimum import find_minimum
import alpha


def main():
    function_index = 4
    method_index = 3
    accuracy = 0.001
    z = 0.1
    result = 0
    x = [3, -1, 0, 1]
    h = [1, 1, 1, 1]
    f = functions.Functions(function_index)

    if method_index == 1:
        def search(b: list):
            temp_b = b.copy()
            tb = f.func(temp_b)
            temp_h = [0] * len(temp_b)

            for itr in range(len(temp_b)):
                temp_he = temp_h.copy()
                temp_he[itr] = h[itr]
                t = f.func(matrix.add(temp_b, temp_he))

                if t < tb:
                    temp_b = matrix.add(temp_b, temp_he)
                    tb = t
                else:
                    temp_he = temp_h.copy()
                    temp_he[itr] = h[itr]
                    t = f.func(matrix.sub(temp_b, temp_he))

                    if t < tb:
                        temp_b = matrix.sub(temp_b, temp_he)
                        tb = t
            return temp_b

        b1 = x.copy()

        while True:
            yk = b1.copy()
            b2 = search(yk)

            while True:
                yk = matrix.add(b1, matrix.mul(matrix.sub(b2, b1), 2))
                y = search(yk)
                b1 = b2.copy()
                if f.func(y) >= f.func(b1):
                    break
                b2 = y.copy()

            if f.func(y) == f.func(b1):
                if matrix.norm(h) <= accuracy:
                    break
                h = matrix.mul(h, z)

        result = b1
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
    print(f.func(result))


if __name__ == '__main__':
    main()
