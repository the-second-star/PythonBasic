a = True
b = False
print (a)
print (b)
x = 3
y = 2
print (x > y) # true (x가 y보다 크다)
print (x < y) # false (x가 y보다 작다)
print (x == y) # false (x가 y와 같다)
print (x != y) # true (x가 y와 같지 않다)
print (x >= y) #true (x가 y보다 크거다 같다)
print (x <=y) #false (x가 y보다 작거나 같다)
# 3x2는 6인가?
print (3 * 2 == 6)
# '*'*2와 '**'는 동일한가?
print ('*'*2 == '**')
print (True and True)
print (True and False)
print (False and True)
print (False and False)
print (True or True)
print (True or False)
print (False or True)
print (False or False)
print (not True)
print (not False)
print (10 == 10 and 10 != 5)
print (10 > 5 or 10 < 3)
print (not 10>= 5)
print (not 10 < 10) 
# not는 결과를 반대로 바꾸기
age = int (input ('나이 : '))
print (age >= 8 and age <= 13)
age = int (input ('나이 : '))
print (age < 8 or age <= 20)
whalecoding = '고래코딩'
print (whalecoding == '고래코딩')
print (whalecoding == 'whalecoding')
print (whalecoding != 'whalecoding')
n = int(input('당신이 가지고 있는 사과의 갯수는? '))
if n == 3: 
    print ('사과를 먹는다')
else:
    print ('사과를 먹지 않는다.')
money = 12000
if money >= 10000:
    print ("택시를 탄다")
else: 
    print ("걷는다")
if True:
    print ("택시를 탄다")
else:
    print ("걷는다")
if False :
    print ("택시를 탄다")
else:
    print ("걷는다")
if 3 < 5:
    print ("True")
if 3 > 5:
    print ("False")
x = 15
if x >= 10:
    print ("10 이상입니다.")
apple = 3
if apple >= 5:
    print ("사과를 나누어 먹는다.")
else:
    print ("사과를 혼자 먹는다.")
money = 10000
if money >= 3000:
    print ("택시를 탄다.")
else: 
    print ("걸어간다.")
answer = input ('게인에서 이겼나요? (yes / no) ')
if answer == 'yes' :
    print ('TV를 보며 편안하게 쉬세요.')
else:
    print ('설거지 당첨!')
number = 15
if number % 3 == 0: 
    print ("{}는 3의 배수입니다.". format (number))
else:
    print ("{}는 3의 배수가 아닙니다.". format (number))
number = 16
if number % 3 == 0: 
    print ("{}는 3의 배수입니다.". format (number))
else:
    print ("{}는 3의 배수가 아닙니다.". format (number))
def upset (s):
    end = ':('
    return (s + ' ' + end) 
s1 = upset ('넘어졌어요') # 넘어졌어요 :(
print (s1)
s2 = upset ('오늘은 조금 피곤해요')
print (s2)
def happy (s):
    end = ':D'
    return (s + ' ' + end)
s1 = happy ('행복해요')
print (s1)
s2 = happy ('코딩 시험 100점 맞았어요')
print (s2)
money = 10000
distance = 100
weather = '비'
if (money >= 1000) and (distance >= 100) and (weather == '비'):
    print ('택시를 탄다')
else:
    print ('걸어간다')
money = int (input ("가지고 있는 돈 : "))
distance = int (input ("목적지와의 거리: "))
weather = input ("닐씨 : ")
if (money >= 10000) and (distance >= 100) and (weather == '비'):
    print ('택시를 탄다')
else:
    print ('걸어간다')
if money >= 10000 or distance >= 100 or weather == '비':
    print ('택시를 탄다')
else:
    print ('걸어간다')
# 택시 - 택시 : 10000, 100, 비
# 걸어 - 택시 : 10000, 100, 해
# 걸어 - 걸어 : 1000, 10, 해
