#-*- coding: utf-8 -*-

score = 0

answer1 = input('Question1')
if answer1 == 'Answer1':
    print('ok')
    score = score + 1
else:
    print('wrong answer')

answer2 = input('Question2')
if int(answer2) == 2:
    print('ok')
    score = score + 1
else:
    print('wrong answer')

answer3 = input('Question3')
if answer3 in ['Answer3', '3']:
    print('ok')
    score += 1
else:
    print('wrong answer')

print('score is %s' % score)
print('You gave {} right answers'.format(score)) #another type of same print
print('Game Over. Bye-Bye!')