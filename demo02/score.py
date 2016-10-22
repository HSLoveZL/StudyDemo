# encoding=utf8
score = input("请输入您的成绩：")
s = int(score)

if 90 <= s <= 100:
    print 'A'
elif 80 <= s < 90:
    print 'B'
elif 70 <= s < 80:
    print 'C'
elif 60 <= s < 70:
    print 'D'
elif s < 60:
    print 'Sorry,your score isn\'t meet the requirement of the exam!'
