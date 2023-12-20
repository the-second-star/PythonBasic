year = input ('당신이 태어난 년도는?')
print (year)
a = int ('2023')
b = float ('36.5')
c = str (2023)
print (a, b, c)
def ready ():
    print ("일어나기")
    print ("밥 먹기")
    print ("이빨 닦고 세수하기")
    print ("옷 입기")
    print ("신발 신고 나가기")
def go ():
    print ("차 타기")
    print ("만나기로 한 곳으로 가기")
    print ("도착하기")
ready ()
go ()
def smile ():
    print ("안녕하세요!")
    print (":D")
smile ()
def operations (a, b):
    print (a + b)
    print (a - b)
    print (a * b)
    print (a / b)
    return operations
ret = operations (10, 5)
print (ret)
def exchange (won):
    return won / 1300
# 함수 호출
print (exchange (20))
print (exchange (100))
print (exchange (365))
dollar = input
print (exchange (dollar))
