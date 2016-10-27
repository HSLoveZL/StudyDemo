# encoding=utf-8
# 删除列表中所有素数元素
from math import sqrt


def deltnum(x):
    for i in range(1, int(sqrt(x))):
        if x/i != 0:
            return x
        else:
            break

print filter(deltnum, [1, 2, 3, 4])
