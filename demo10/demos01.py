# coding=utf-8
# 哈希算法
import hashlib

md5 = hashlib.md5()
md5.update('hello,world1')
print md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('how to use sha1?')
sha1.update('It\'s easy!')
print sha1.hexdigest()
