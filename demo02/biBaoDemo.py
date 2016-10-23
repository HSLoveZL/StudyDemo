# encoding=utf-8
# 函数的闭包方法


def func01(x):
    def func02(y):
        return x * y
    return func02


print func01(8)(5)


def fun02():
    x = [5]

    def fun03():
        x[0] *= x[0]
        return x[0]
    return fun03()
print fun02()


def fun04():
    x1 = 5

    def fun05():
        nonlocal x1
        x1 *= x1
        return x1
    return fun05()
