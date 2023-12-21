def func1():
    print("A")
    print("B")
def func2():
    print("C")
    print("D")
def func3():
    print("E")
    return "F"
func1()
print("0")
print(func3())
func2()
print("1")
func1()
func3()
# ABCD0EFFCD1ABEF
a = True
b = False
# c = true
# d = false
# e = TRUE
# f = FALSE
x = 10 
y = 8
print(x > y) # true
print(x < y) # false
print(x == y) # false
print(x != y) # true 
print(x >= y) # true
print(x <= y) # false
print(x/10 < y) #true
whalecoding = '고래코딩'
print(whalecoding == '고래코딩') # true
print(whalecoding == 'whalecoding') # false
print(whalecoding != 'whalecoding') # true
whalecoding = 'whalecoding'
print(whalecoding == '고래코딩') # false
print(whalecoding == 'whalecoding') # true
print(whalecoding != 'whalecoding') # false
print(10 == 10 and 10 != 5) # true and true
print(10 > 5 or 10 < 3) # true and false
print(not 10 >= 5) # false
print(not 10 < 10) # true
print((3 == 3) or (4 != 3)) # true
print((3 == 3) and (4 != 3)) # true and true
age = int(input('나이 : '))
print (age >= 8 and age <= 13)
if 10 < 8:
    print("고래")
else:
    print("코딩")
print("1")
if True :
    print("2")
else :
    if False:
        print("3")
    else:
        print("4")
print("5")
print("1")
if True :
    if False:
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
number = int(input('숫자 : '))
if number % 2 == 0:
    print("{}는 짝수". format (number))
else:
    print("{}는 홀수". format (number))
x = 5 
if x != 10:
    print('ok')
num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
if num1 > num2 and num3:
    print (num1)
if num2 > num1 and num3:
    print (num2)
if num3 > num1 and num2:
    print (num3)
