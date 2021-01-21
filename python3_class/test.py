def f(x):
    return x ** 5


def diff2(f, x, h=1e-5):
    dif = (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
    return dif


print(diff2(f, 1))
