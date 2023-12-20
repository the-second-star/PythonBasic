print ("나는 사과 {0}개를 먹었다.".format(5))
print ("나는 사과 {0}개를 먹었다.".format(100))
print ("나는 사과 {0}개를 먹었다.".format(1000))
s = "나는 사과 {0}개를 먹었다."
print (s.format (1000))
n = 1000
print (s.format (n))
print (s.format ("다섯"))
number_of_apples = 3
location = "학교"
print ("나는 사과 {0}개를 먹었다.".format (number_of_apples, location))
print ("나는 사과 {0}개를 먹었다. 그리고 {1}에 갔다.".format (number_of_apples, location))
print ("나는 사과 {1}개를 먹었다. 그리고 {0}에 갔다.".format (number_of_apples, location))
print ("나는 사과 {}개를 먹었다. 그리고 {}에 갔다.".format (number_of_apples, location))
print ("나는 사과 {0}개를 먹었다. 그리고 {1}에 갔다.".format (number_of_apples + 1, location + '와 학원'))
# s = input ('사과의 개수는?')
# print ('사과의 개수는 {}개 입니다.'.format (s))
# age = input ('당신의 나이는?')
# print (age)
# name = input ('당신의 이름은?')
# print (name)
# print (age)
# age = int(age)
# print ('당신은 올해 {}살 입니다.'.format (age))
# print ('당신은 내년 {}살 입니다.'.format (age + 1))
# print ('당신의 이름은?')
# name = input ()
# print (name)
# name = input ('당신의 이름은?')
# age - int (input ('당신의 나이는?'))
# print ('당신은' + name + '이고' + str(age) + '살입니다.')
# print ('당신은', name, '이고' + str(age) + '살입니다.')
# print ('당신은 {} 이고 {}살 입니다.'. format (name, age))
# date = input ('오늘 날짜 :')
# year = date [0:4]
# month = date [5:7]
# day = date [8:10]
# print ('년 :', year)
# print ('월 :', month)
# print ('일 :', day)
# s. format (___) 혹은 f'___' 사용
s = '오늘의 평균 기온은 {}도 입니다.'
print (s. format ('-9.4C֯ '))
s1 = '좋은 아침입니다.!'
s2 = s1 [0:5] + s1 [9:10]
print (s2)
def 시리얼먹기 (우유, 시리얼, 그릇, 숟가락):
    # 우유 = "서울우유"
    # 시리얼 = "콘푸로스트"
    # 그릇 = "밥그릇"
    # 숟가락 = "쇠숟가락"
    print ("준비물을 준비합니다.")
    print ("{}을 {}에 넣습니다.". format (시리얼, 그릇))
    print ("{}를 {}이 담긴 {}에 따릅니다.". format (우유, 시리얼, 그릇))
    print ("{}으로 {}과 {}를 떠서 먹습니다.". format (숟가락, 시리얼, 우유))
# 함수 호출
print("*" * 100)
시리얼먹기 ("서울우유", "콘푸로스트", "밥그릇", "쇠숟가락")
시리얼먹기 ("2% 우유", "책스 초코", "냄비그릇", "은숟가락")
# 시리얼먹기 ("우유", "시리얼", "그릇", "숟가락")
# 시리얼먹기 ("우유", "시리얼", "그릇", "숟가락")
def 시리얼먹기 (우유, 시리얼, 그릇, 숟가락):
    print ("준비물을 준비합니다.")
    print ("{}을 {}에 넣습니다.". format (시리얼, 그릇))
    print ("{}를 {}이 담긴 {}에 따릅니다.". format (우유, 시리얼, 그릇))
    print ("{}으로 {}과 {}를 떠서 먹습니다.". format (숟가락, 시리얼, 우유))
    return "{} 1 리터, {} 500 그램 남았습니다.". format (우유, 시리얼)
print("*" * 100)
시리얼먹기 ("서울우유", "콘푸로스트", "밥그릇", "쇠숟가락")
시리얼먹기 ("2% 우유", "책스 초코", "냄비그릇", "은숟가락")
결과 = "{} 1 리터, {} 500 그램 남았습니다.". format ("우유", "시리얼")
print (결과)
def add (a, b):
    return a + b

a = 3
b = 4
c = add (a, b)
print (c)
print (add (10, 15))
print (add (2345899, 194943))
print (add (3, 100000000000))
def message (): 
    print ("A")
    print ("B")
message ()
print ("C")
message ()
def error ():
    print (("error" + " ") * 3)
error ()
def say1 (name):
    string = '안녕하세요?' + ' ' + name + '님'
    return string
def say2 (name):
    string = '안녕하세요?' + ' ' + name + '님'
    print (string)
name = "홍길동"
say1 (name)
say2 (name)
def 더하기 (a, b):
    return a + b
def 빼기 (a, b):
    return a - b
def 곱하기 (a, b):
    return a * b
def 나누기 (a, b):
    return a / b
a = 6
b = 3
print (더하기 (a, b))
print (빼기 (a, b))
print (곱하기 (a, b))
print (나누기 (a, b))
# 함수 정의
def exchange (won):
    return won / 1300
# 함수 호출
print (exchange (1300))
print (exchange (13000))
print (exchange (100000))
