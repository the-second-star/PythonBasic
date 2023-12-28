print ("'python'은 프로그래밍 언어입니다.")
farenheight = int (input ('화씨 온도는?'))
celsius = int (input ('섭씨 온도는?'))
f_to_c = (farenheight - 32) / 1.8
c_to_f = (celsius * 1.8) +32
print('화씨 {}도는 섭씨 {}도'.format(farenheight, f_to_c))
print('섭씨 {}도는 화씨 {}도'.format(celsius, c_to_f))
year = int (input ('올해의 년도는?'))
print ('Hello world!')
print ("Hello world!")
# print (''Hello world!'') : 실행 불가능
# print (""Hello world!"") : 실행 불가능
print ('''Hello world!''')
print ("""Hello world!""")
s1 = 'hello'
s2 = 'world'
print ((s1 + ' ' + s2 + ' ') * 5)
a = 2023
b = 12
print (a + b) # 2035
a = "2023"
b = "12"
print (a + b) # 202312
s = 'Love yourself.'
print (s [0])
print (s [2]) 
print (s [7])
print (s [9])
print (s [12])
sentence = "Python에서 숫자 10과 문자 '10'은 다르다."
print (sentence [5]) # n
print (sentence [-5]) # space
print (sentence [10:12]) # 자 space
print (sentence [13:]) # 0과 문자 '10'은 다르다.
s = '공격받은 몬스터는 {}의 데미지를 받았습니다.'
print (s. format (10))
print (s. format (50))
print (s. format (297))
# age = 12
# age [0] : 숫자는 이 형식을 쓸 수 없어서 error가 난다.
age = '12'
age [0]
age = int (input ('당신은 올해 몇살 입니까?'))
year = (int (input ('올해의 년도는?'))) - age
print('당신의 올해 나이는 {}살 입니다. 당신은 {}년에 태어났습니다.'.format(age, year))
s = input ('오늘을 이 형식으로 입력해주세요. : 20240101Sunny : ')
year = s [0:4]
month = s [4:6]
day = s [6:8]
weather = s [8: ]
print ("{}년 {}월 {}일 / 날씨 : {}". format (year, month, day, weather))
def smile (s):
    end = ':D'
    print (s + end)
s = '안녕하세요'
n = '날씨가 좋아요'
(smile (s))
(smile (n))
def upset(s):
    end = ':('
    return (s + end)
s1 = '넘어졌어요'
s2 = '오늘은 조금 피곤해요'
print (upset (s1))
print (upset (s2))
def exchange (won) :
    return won / 1300
print ('${}'.format(exchange(1300))) 
print ('${}'.format(exchange(2600))) 
print ('${}'.format(exchange(13000))) 
print ('${}'.format(exchange(1000000))) 
won = int (input ('환전할 원화 : '))
dollar = exchange (won)
print ('당신은 ${} 를 환전했습니다.'.format (round (dollar, 5)))
a = True
b = False
# c = true : does not work
# d = false : does not work
# e = TRUE : does not work
# f = FALSE : does not work
x = 4 
y = 9
print (x > y) # false
print (x < y) # true
print (x == y) # false
print (x != y) # true
print (x >= y) # false
print (x <= y) # true
print (x/10 < y) # true
print (10 == 10 and 10 != 5) # true
print (4 > 2 and 7 == 3) # true
print (10 < 5 or 10 > 3) # true
print (9 < 7 or 7 < 3) # false
print (not 10 >= 5) # false
print (not 10 <= 10) # false
print("1")
if True:
    print("2")
else :
    print("3")
print("4") # 124
print("1")
if 3 > 7:
    if 10 == 9:
        print("2")
    else:
        print("3")
else :
    print("4")
print("5") # 145 
print("1")
if 'coding' == 'coding':
    if 'whale' == 'Whale':
        print("2")
    elif 3 != 3:
        print("3")
    else:
        print("4")
elif 3 == 3:
    print("5")
else :
    print("6")
print("7") # 147
def even_odd(number):
    if number % 2 == 1:
        print("홀수")
    else:
        print("짝수")
number = input("숫자 입력 : ")
even_odd (int (number))
num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
# 코드 작성
if num1 < num2 and num1 < num3:
    print('{}이 가장 작은 숫자입니다.'.format(num1))
elif num2 < num1 and num2 < num3:
    print('{}이 가장 작은 숫자입니다.'.format(num2))
elif num3 < num1 and num3 < num2:
    print('{}이 가장 작은 숫자입니다.'.format(num3))
else:
    print('같은 숫자가 2개 이상 입니다.')
def print_price(transportation):
    adult_price = 0
    if transportation == 'bus':
        adult_price = 50000
    if transportation == 'ship':
        adult_price = 70000
    if transportation == 'airplane':
        adult_price = 100000
    child_price = adult_price / 2
    print('{}의 성인 요금은 {}원, 어린이 요금은 {}원 입니다.'.format (transportation, adult_price, child_price))
transportation = input("사용할 교통편: bus / ship / airplane: ")
print_price(transportation)
for i in range(1, 101, 1):
    if i % 7 == 0:
        print (i)
i = 0
while i <= 100:
    i = i + 1
    if i % 7 == 0:
        print(i)
while True:
    capital = input('한국의 수도는? : ')  
    if capital == '그만' : 
        break
    elif capital == '서울':
        print ('정답!')
while True:
    score = int (input("점수: "))
    if score >= 80:
        print ('A 등급')
    elif score >= 60:
        print ('B 등급')
    elif score >= 40:
        print ('C 등급')
    elif score >= 20:
        print ('D 등급')
    elif score >=0:
        print ('E 등급')
    elif score -1:
        break
    else:
        print ('잘못된 입력')
while True:
    age = int(input('나이 : '))
    if age >= 8 and age <= 13:
        print ('초등학생 입니다.')
    elif age >= 13 and age <= 16:
        print ('중학생 입니다.')
    elif age >= 17 and age <= 19:
        print ('고등학생 입니다.')
    elif age < 8 and age > 0:
        print ('미취학 아동 입니다.')
    elif age > 20:
        print ('성인 입니다.')
    elif age == -1:
        break
# a = 1000 : int
# b = '1000' : str
# c = True : bool
# d = 'False' : str
# e = 'hello world!' : str
# # f = TRUE : error
# g = 30.1 : int
# h = '2023' : str
# # i = true : error
# j = 'false' : str
# k = -59 : int
# l = 0 : int
# m = '0' : str
# n = '2023'+'11' : str
# o = False : bool
# p = 1000 + 100 - 99 : int
# q = '*' * 10 : bool
# r = 10 * 10 : int
# s = '100' <= 10 : bool
# t = 100 > 10 : bool
# # u = false : error
number = int (input ('숫자 입력: '))
for i in range (number):
    print ('*' * number)
n = int (input ('별 몇 개?: '))
for i in range (1, (n + 1), 1):
    print ('*' *  i)
n = int (input ('별 몇 개?: '))
for i in range (1, n+1, 1):
    print (' ' * (n - i) + '*' * i)
n = int (input ('별 몇 개?: '))
for i in range (0, n, 1):
    print (' ' * (n - i) + '*' * (i * 2 + 1))
def operations(num1, num2):
    r1 = num1 + num2
    r2 = num1 - num2
    r3 = num1 * num2
    r4 = num1 / num2
    print ('{} + {} = {}'.format(num1, num2, r1))
    print ('{} - {} = {}'.format(num1, num2, r2))
    print ('{} x {} = {}'.format(num1, num2, r3))
    print ('{} / {} = {}'.format(num1, num2, r4))
    return r1+r2+r3+r4
# 함수 호출
num1 = int (input ('첫번째 숫자를 입력해주세요.'))
num2 = int (input ('두번째 숫자를 입력해주세요.'))
result = operations (num1, num2)
print (result)
# 90 / 100
