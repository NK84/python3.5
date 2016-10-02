#-*- coding: utf-8 -*-

score = 0

def validate_answer(user_answer, valid_answer):
    global score

    if user_answer == valid_answer:
        print('ok')
        score += 1
    else:
        print('wrong answer')

#database = {
#    'Question1': 'Answer1',
#    'Question2': 2,
#    'Question3': '3',
#}

#for question, answer in database.items():
#    print(question, answer)

answer1 = input('Question1')
validate_answer(answer1, 'Answer1')

answer2 = input('Question2')
validate_answer(int(answer2), 2)

answer3 = input('Question3')
validate_answer(answer3, '3')

print('score is %s' % score)
print('You gave {} right answers'.format(score)) #another type of same print
print('Game Over. Bye-Bye!')

