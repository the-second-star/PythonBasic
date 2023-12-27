i = 0
add = 0
while i <= 9:
    i = i + 1
    print (i)
    if i == i:
        add = add + i
print (add)
result = 0
for i in range (1, 11, 1):
    print (i)
    result = result + i
print (result)
i = 1
add = 1
while i <= 9:
    i = i + 1
    print (i)
    if i % 2 == 1:
        add = add + i
print (add)
result = 0
for i in range (1, 11, 1):
    print (i)
    if i % 2 == 1:
        result = result + i
print (result)
i = 1
add = 1
while i <= 9:
    i = i + 1
    print (i)
    if i == i:
        add = add * i
print (add)
s = 5
print ('*' * (s-4))
print ('*' * (s-3))
print ('*' * (s-2))
print ('*' * (s-1))
print ('*' * s)
print ('-----')
print ('*' * s)
print ('*' * (s-1))
print ('*' * (s-2))
print ('*' * (s-3))
print ("*" * (s-4))
s = int (input ('별 몇 개?: '))
for s in range (1, (s+1), 1):
    print ('*' * s)
for i in range (1, 6, 1):
    print ('*' * i)
for i in range (5, 0, -1):
    print ('*' * i)
for i in range (3, 21, 3):
    print (i)
for i in range (1, 11):
    print (i)
for i in range (10):
    print (i)
for i in range (10, 0 -1):
    print (i)
score = int (input ('당신의 점수는?'))
if score >= 60:
    print ('합격 했습니다.')
elif score <= 60:
    print ('불합격 입니다.')
elif score == '-1':
    # break
    print ('종료 되었습니다.')
cap = input ('한국의 수도는?: ')
if cap == '서울':
    print ('맞습니다!')
else:
    cap = input ('다시 도전해 보실레요? 도전 / 그만: ')
if cap == '그만':
    # break
    print ('종료 되었습니다.')
n = int (input ('숫자를 입력해주세요.'))
if n % 7 == 0:
    print ('이 숫자는 7의 배수 입니다.')
else: 
    print ('이 숫자는 7의 배수가 아닙니다.')
score = int (input ('점수: '))
if 81 <= score:
    print ('A 등급')
elif 61 <= score and 80 >= score:
    print ('B 등급')
elif 41 <= score and 60 >= score:
    print ('C 등급')
elif 21 <= score and 40 >= score:
    print ('D 등급')
else:
    print ('E 등급')
# for True: 
# for False:
# while True: loop
# while False: loop
title = '1, 2, 아니면 3?'
if title == 1:
    for number in range (1, 10):
        string = '{} x {} = {}'. format (1, number, 1 * number)
    print (string)
    string = '{} x {} = {}'. format (3, number, 3 * number)
    print (string)
    string = '{} x {} = {}'. format (5, number, 5 * number)
    print (string)
    string = '{} x {} = {}'. format (7, number, 7 * number)
    print (string)
    string = '{} x {} = {}'. format (9, number, 9 * number)
elif title == 2:
    for number in range (1, 10):
        string = '{} x {} = {}'. format (2, number, 2 * number)
    print (string)
    string = '{} x {} = {}'. format (4, number, 4 * number)
    print (string)
    string = '{} x {} = {}'. format (6, number, 6 * number)
    print (string)
    string = '{} x {} = {}'. format (8, number, 8 * number)
elif title == 3:
    # break
    print ('종료 되었습니다.')
number = int (input('숫자를 입력하세요.'))
for i in range (number):
    print ('I love Python')
for x in range (2002, 2051, 4):
    print (x)
for i in range (10):
    if i == 7:
        break 
    print ("The Number is :" , i)
n = int (input ('N 값을 입력해주세요: '))
for i in range (2, n+1):
    is_prime = True   
    for i in range (1, n, 2):
        if i == 0:
            is_prime = False   
    if is_prime:
        print(i, end=' ')
