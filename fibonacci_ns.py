
def convert(number):
    fibs = [1]
    next_fib = 2

    while next_fib <= number:
        fibs.append(next_fib)
        next_fib = fibs[-1] + fibs[-2]

    result = []
    for fib in reversed(fibs):
        if number >= fib:
            number -= fib
            result.append(1)
        else:
            result.append(0)

    return result


def convert_to_dec(array):
    result = 0

    fib_first, fib_second = 1, 2
    for item in reversed(array):
        result += item * fib_first
        tmp = fib_first + fib_second
        fib_first = fib_second
        fib_second = tmp

    return result
