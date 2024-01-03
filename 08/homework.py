born_year = int (input ('당신이 태어난 년도는?'))
current_year = int (input ('지금 년도는?'))
age = current_year - born_year
print (age)
def say1(name):
    string = '안녕하세요? ' + name + '님'
    return string
def say2(name):
    string = '안녕하세요? ' + name + '님'
    print(string)
name = "홍길동"
string = say1 (name)
print (string)
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
print (더하기 (b, a))
print (빼기 (b, a))
print (곱하기 (b, a))
print (나누기 (b, a))
def add_10 (number):
    return number + 10
a = 100
result = add_10 (a)
print (result)
result2 = add_10 (result)
print (result2)
def smile (s):
    return s + ':D'
print (smile ('안녕하세요'))
def exchange (dollar):
    return dollar * 1300
print (exchange (20))
print (exchange (100))
print (exchange (365))
dollar = int (input ('How many USD would you like to exchange into KRW?'))
print (exchange (dollar)) 
