n = int (input ('별 몇 개?: '))
for i in range (1, n+1, 1):
    print (' ' * (n - i) + '*' * i)
n = int (input ('별 몇 개?: '))
for i in range (0, n, 1):
    print (' ' * (n - i) + '*' * (i * 2 + 1))
while True:
    score = int (input ('점수: '))
    if score == -1:
        break
    if score >= 60:
        print ('합격')
    if score <= 59:
        print ('불합격')
