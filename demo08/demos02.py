#!/usr/bin/python2.7
class Student(object):
    

    def __init__(self, name, score):
        self.name = name
        self.score = score


    def print_score(self):
        print '%s: %s' % (self.name, self.score)

a = Student('HongSh', 98)
b = Student('Zhanglei', 94)
a.print_score()
b.print_score()

