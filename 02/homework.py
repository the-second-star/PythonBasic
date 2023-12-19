# age 라는 이름 가진 변수를 만들고
# 11 이라는 값을 할당해주세요.
age = 11
print (age)
print ('안녕 파이썬!')
print ("안녕 파이썬!")
# print (''안녕 파이썬!'') : print 불가능
# print (""안녕 파이썬!"") : print 불가능
print ('''안녕 파이썬!''')
print ("""안녕 파이썬!""")
s1 = "변수"
s2 = "할당"
s3 = s1 + ' ' + s2 + ' '
print (s3 * 3)
sentence = "여의도역으로 가는 길은 어디인가요?"
print (sentence[5])
print (sentence[-5])
print (sentence[10:12])
print (sentence[13:])
# s.format(____) 혹은 f'____' 사용
s = '오늘의 평균 기온은 -9.4C֯ 도 입니다.'
print (s)
s = "나는 사과 {}개를 먹었다.".format(3)
print (s)
print ("나는 사과 {}개를 먹었다.".format(5))
print ("나는 사과 {}개를 먹었다.".format("열"))
print ("나는 사과 {}개를 먹었다.".format(100))
print ("나는 사과 {}개를 먹었다.".format("이백"))
# print("나는 사과 {}개를 먹었다.".format(다섯)): 오류 이유= 다섯에 " 나 ' 가 없어서
s1 = "나는 오늘 학교에 갔다."
s2 = "나는 오늘 학원에 갔다."
s3 = "나는 오늘 놀이동산에 갔다."
print (s1)
print (s2)
print (s3)
age = 11
# print (age [0]) # number형은 index 접근 불가능
age = '11'
# print (age [0]) # number형은 index 접근 불가능
a = '' # string
b = "Nice to meet you." # string
c = 2023 # number
d = '''안녕하세요^^''' # string
e = '2023/10' # string
f = """Hello world!""" # string
g = 202310 # number
h = 123 # number
i = '123' # string
j = 0 # number
k = '''프로그래밍 언어는 다양하다.
파이썬은 프로그래밍 언어이다.''' # string
l = "\n" # string
a = 2023
b = 12
print(a + b) # 2035
a = "2023"
b = "12"
print(a + b) # 202312
