# coding=utf-8
# 删除列表中所有素数元素
from math import sqrt


def is_prime(n):
    flag = 0
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            flag = 1
            break
    if flag == 1:
        return n

print filter(is_prime, range(1, 101)),
