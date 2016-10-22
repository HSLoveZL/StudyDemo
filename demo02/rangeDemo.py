# encoding=utf-8

for i in range(2, 9):
    print i
for i in range(2, 9, 2):
    print i


temp = ('mary', 'bob', 'david', 'hah')
temp1 = temp[:2] + ('hongsh', ) + temp[2:]
print temp1


def func(name):
    print name + '你好！'
func('HongShuai')
