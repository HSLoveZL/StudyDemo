# coding=utf-8
def fac(n):
    result1 = n
    for i in range(1, n):
        result1 *= i
    return result1

number = int(input('请输入一个整数：'))
result = fac(number)
print result
