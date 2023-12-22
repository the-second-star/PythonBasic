written_test = 75
coding_test = True
if written_test >= 80 and coding_test == True:
    print ('합격')
else:
    print ('불합격')
hamburger_shop = 'closed'
tteokbokki_shop = 'closed'
convenience_store = 'closed'
house = 'closed'
if hamburger_shop == 'open':
    print ('햄버거를 먹는다')
elif tteokbokki_shop == 'open':
    print ('떡볶이를 먹는다')
elif convenience_store == 'open':
    print ('편의점에서 라면을 먹는다')
elif house == 'open':
    print ('집에 간다')
else:
    print ('집 열쇠를 실수로 집에 두고 와서 도둑이 된다')
score =int (input ("점수: "))
if 81 <= score:
    print ('A 등급')
elif 61 <= score and 80 >= score:
    print ('B 등급')
elif 41 <= score and 60 >= score:
    print ('C 등급')
elif 21 <= score and 40 >= score:
    print ('D 등급')
else:
    print ('F 등급')
score = 85
if 81 <= score:
    print ("훌륭해요!")
if 61 <= score:
    print ("잘했어요!")
if 41 <= score:
    print ("열심히 했군요!")
else: 
    print ("조금 더 노력합시다!")
score = 85
if 81 <= score:
    print ("훌륭해요!")
elif 61 <= score:
    print ("잘했어요!")
elif 41 <= score:
    print ("열심히 했군요!")
else: 
    print ("조금 더 노력합시다!")
hit = 0
s = '나무를 {}번 찍었습니다.'
while hit < 10:
    hit = hit + 1
    print (s. format (hit))
    if hit == 2:
        print ('아주 약하시군요. 나무가 꿈쩍 하지도 않습니다.')
    elif hit == 5:
        print ('힘을 좀 쓰고 계시네요. 나무가 조금 흔들리고 있습니다.')
    elif hit == 8:
        print ('나무가 넘어갈 것 같습니다.')
    elif hit == 10:
        print ('나무가 넘어갔습니다.')
        print ('나무는 죽었고 그것은 당신의 탓 입니다.')
        print ('엇, 죽지 않았네요. 단단히 화가난 나무가 망치를 들고 뛰쳐오고 있습니다. 살아 있는것이 좋거나 목숨을 아끼신다면 도망가세요.')
number = 0
while number != 100:
    print ('100 입력시 프로그램 종료')
    number = int (input ('숫자: '))
# number = 0
# while True:
#     number = number + 1
#     print (number)
number = 1
while number <= 10:
    print (number)
    number = number + 1
number = 0
max = int (input ())
while number < max:
    number = number + 1
    print (number)
print ('숫자 두 개를 작은수부터 입력해주세요.')
min = int (input ())
max = int (input ())
while min <= max:
    print (min)
    min = min + 1
