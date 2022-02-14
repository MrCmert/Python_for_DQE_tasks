def factorial(n):
    """
    :param n: input number
    :return: value of factorial of this number
    """
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(3))


def fibo(n):
    """
    :param n: number in the fibonacci sequence
    :return: the value of a number in the fibonacci sequence
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(10))
