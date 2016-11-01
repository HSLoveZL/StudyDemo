#!/usr/bin/python2.7
class Student(object):


    def __init__(self, name, score):
	self.__name = name
	self.__score = score


    def get_name(self):
	return self.__name


    def set_name(self, name):
	self.__name = name


    def get_score(self):
	return self.__score


    def set_score(self, score):
	self.__score = score


    def print_score(self):
	print '%s: %s' % (self.__name, self.__score)


std = Student('HongSh', 98)
std.print_score()

