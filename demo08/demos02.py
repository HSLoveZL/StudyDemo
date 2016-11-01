#!/usr/bin/python2.7
class Student(object):
    

    def __init__(self, name, score):
        self.name = name
        self.score = score


    def print_score(self):
        print '%s: %s' % (self.name, self.score)


    def score_grade(self):
        if (self.score >= 90):
            print 'A'
	elif (80 <= self.score < 90):
	    print 'B'

a = Student('HongSh', 98)
b = Student('Zhanglei', 94)
a.print_score()
b.print_score()
a.score_grade()
b.score_grade()

