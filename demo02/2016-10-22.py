# encoding=utf-8
def discount(price, rate):
    final_price = price * rate
    return final_price


p = int(input('请输入现有的价格:'))
r = float(input('请输入现在的折扣:'))

new_price = discount(p, r)
print '打折后的价格为：', new_price
