# encoding=utf-8
def func1():
    print '函数1正在被调用'

    def func2():
        print '函数2正在被调用'

    func2()
func1()
