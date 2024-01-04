l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (len (l1))
t1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (len (t1))
s1 = "123456789012345678901234567890"
print (len (s1))
string = '안녕하세요'
for i in range (len (string)):
    print (string [i])
list1 = ['리', '스', '트', 1, 2, 3]
for i in range (len (list1)):
    print (list1 [i])
tuple1 = ('튜', '플', 4, 5, 6)
for i in range (len (tuple1)):
    print (tuple1 [i])
학생수 = 5
성적 = [0] * 학생수
이름 = ['홍길동', '김철수', '이영희', '성춘향', '이몽룡']
for i in range (학생수):
    성적 [i] = int (input ('{} 학생의 성적을 입력하세요: '. format (이름 [i])))
for i in range (학생수):
    print ('{} 학생의 성적: {}'. format (이름 [i], 성적 [i]))
string1 = '안녕하세요'
for c in string1:
    print (c)
list1 = ['리', '스', '트', 1, 2, 3]
for var in list1:
    print (var)
tuple1 = ('튜', '플', 4, 5, 6)
for var in tuple1:
    print (var)
scores = [90, 25, 67, 45, 80, 45, 76, 34, 6, 14]
number = 0
for score in scores:
    number = number + 1
    if score >= 60:
        print ('{}번 학생은 합격입니다.'. format (number))
    else:
        print ('{}번 학생은 불합격 입니다.'. format (number))
i = 0
for letter in ['A', 'B', 'C']:
    print (i, letter)
    i += 1
letters = ['A', 'B', 'C']
for i in range (len (letters)):
    letter = letters [i]
    print (i, letter)
for entry in enumerate (['A', 'B', 'C']):
    print (entry)
for entry in enumerate (['A', 'B', 'C']):
    print (i, letter)
