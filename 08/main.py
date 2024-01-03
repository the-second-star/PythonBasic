학생수 = 5
성적 = [1] * 학생수
for 번호 in range (학생수):
    성적 [번호] = int (input ('{}번 학생의 성적을 입력하세요: '. format (번호)))
for 번호 in range (학생수):
    print ('{}번 학생의 성적: {}'. format (번호, 성적 [번호]))
a = []
b = [1, 2, 3]
c = ['안녕', '하세요']
d = [1, 2, '오늘은', '맑음']
e = [1, 2, ['안녕!', '파이썬']]
list1 = [1, 2, 3, 4, 5]
print (list1)
scores = [10, 50, 20 , 60]
print (scores[1]) # 10
print (scores[-1]) # 60
print (scores[2 : 4]) # 20, 60
print (scores[1 : 3]) # 50, 20
print (scores[2 : ]) # 20, 60
print (scores[ : 2]) # 10, 50
a = [1, 2, 3]
b = [4, 5, 6]
print (a + b) # 1, 2, 3, 4, 5, 6
a = [1, 2, 3]
print (a * 3) # 1, 2, 3, 1, 2, 3, 1, 2, 3
list1 = []
print (list1)
subject = ['국어', '수학', '영어', '과학']
print (subject)
scores = [86, 75, 64, 99, 100, 82, 70, 93]
print (scores [3])
print (scores [5])
print (scores [-2])
print (scores [1 : 4])
무지개 = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
첫번째색 = 무지개 [0]
print ('무지개의 첫본째 색은 {}이다'. format (첫번째색))
무지개 = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
마지막색 = 무지개 [6]
print ('무지개의 첫본째 색은 {}이다'. format (마지막색))
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print (list3)
동물 = ['강아지', '고양이', '새', '코끼리', '곰']
식물 = ['소나무', '단풍나무', '장미꽃', '벚꽃']
생물 = 동물 + 식물
print (생물)
score = [10, 59, 93, 76]
score. append (80)
print (score) # 10, 59, 93, 76, 80
score = [10, 59, 93, 76]
score = score + [80]
print (score) # 10, 59, 93, 76, 80
score = [10, 59, 93, 76]
score. insert (2, 40)
print (score) # 10, 59, 40, 93, 76
score. insert (4, 80)
print (score) # 10, 59, 40, 93, 80, 76
score = [10, 59, 93, 76]
score [0] = 100
print (score) # 100, 59, 93, 76
score = [10, 59, 93, 76]
del score [0]
print (score) # 59, 93, 76
score = [10, 59, 93, 76]
score. remove (10)
print (score) # 59, 93, 76
score = [10, 59, 93, 76, 10]
score. remove (10)
print (score) # 59, 93, 76, 10
animals = ['강아지', '고양이', '새', '코끼리', '소나무']
animals [4] = '고래'
print (animals)
animals. append ('사람')
print (animals)
animals = ['강아지', '고양이', '새', '코끼리', '고래']
animals. insert (3, '돼지')
print (animals)
animals = ['강아지', '고양이', '새', '코끼리', '고래']
del animals [0]
print (animals)
animals = ['강아지', '고양이', '새', '코끼리', '고래']
animals. remove ('강아지')
print (animals)
a = ()
b = (1, 2, 3)
c = ('안녕', '하세요')
d = (1, 2, '오늘은', '맑음')
e = (1, 2, ('안녕!', '파이썬'))
f = 1, 2
# t = (1, 2, 3, 4)
# del t [0]
# t = (1, 2, 3, 4)
# t [0] = 'c'
t = (1, 2, 3, 4)
print (t [0])
print (t [3])
print (t [1 : ])
print (t [1 : 3])
tuple1 = ()
print (tuple1)
foods = ('짜장면', '떡볶이', '된장찌개', '햄버거', '피자', '김밥')
print (foods)
scores = (100, 82, 70, 86, 64, 99, 93)
print (scores [3])
print (scores [5])
print (scores [-2])
print (scores [1 : 4])
무지개 = ('빨강', '주황', '노랑', '초록', '파랑', '남색', '보라')
첫번째색 = 무지개 [0]
print ('무지개의 첫본째 색은 {}이다'. format (첫번째색))
무지개 = ('빨강', '주황', '노랑', '초록', '파랑', '남색', '보라')
마지막색 = 무지개 [6]
print ('무지개의 첫본째 색은 {}이다'. format (마지막색))
# 동물 = ('강아지', '고양이', '새', '코끼리', '곰')
# 동물 [0] = '사람'
# del 동물 [0]
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print (t * 10)
list = []
movies = ['보스베이비', '어벤져스', '찰리와 초콜릿 공장', '슈퍼배드']
movies. append ('겨울왕국2')
movies. insert (4, '겨울왕국')
del movies [1]
movies. remove ('찰리와 초콜릿 공장')
language1 = ["c", "C++", "Java"]
language2 = ["Python", "Go", "C#"]
languages = language1 + language2
tuple = ()
movies = ('보스베이비', '어벤져스', '찰리와 초콜릿 공장', '슈퍼배드')
# movies = ('보스베이비', '어벤져스')
# movies [0] = '슈퍼배드'
data = int (input ("1, 2, 3을 입력해주세요."))
rpc = ('바위, 보, 가위')
print (rpc)
rpc = ('바위, 보, 가위')
while True:
    data = int (input ("1, 2, 3을 입력해주세요."))
    if data == -1:
        break
