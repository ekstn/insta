from random import randrange

a = int(input('답을 입력해 주세요 : '))
b = randrange(1, 1000)
life = 15

while b != a:
    if a < b:
        print(f'{a}보다 큽니다.')
        a = int(input('답을 다시 입력해 주세요 : '))
    else:
        print(f'{a}보다 작습니다.')
        a = int(input('답을 다시 입력해 주세요 : '))


print('정답입니다.')
