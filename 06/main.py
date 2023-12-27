number = 0
while number < 10:
   number = number + 1
   print (number)
for i in range (1, 11, 1):
   print (i)
for i in range (1, 13, 1):
   print ("{}월". format (i))
for i in range (3):
   print ("세번 출력")
print ('숫자 두 개를 작은수부터 입력해주세요.')
min = int (input ())
max = int (input ())
for i in range (min, max + 1, 1):
   print (i)
max = int (input ())
for i in range (1, max + 1, 3):
   print (i)
max = int (input ())
for i  in range (max):
   print ('안녕하세요')
for i in range (1, 11):
   print ('나무를 {}번 찍었습니다.'. format (i))
for i in range (3):
   print (i)
i = 0 
while i <= 2:
   print (i)
   i += 1
for number in range (4):
   if number == 2:
      continue
   print (number)
for number in range (4):
   if number == 2:
      break
   print (number)
number = 0
while number < 10:
   number = number + 1
   if number % 2 == 0:
      continue
   print (number)
number = 0
while number < 10:
   number = number + 1
   if number == 5:
      print ('{}입니다.'. format (number))
      break
   print (number)
while True:
   data = input ('입력: ')
   if data == '그만':
      break
for number in range (1, 10):
   string = '{} x {} = {}'. format (2, number, 2 * number)
   print (string)
for number in range (1, 10):
   string = '{} x {} = {}'. format (9, number, 9 * number)
   print (string)
단 = int (input ('구구단을 출력합니다. 몇 단인지 입력해주세요'))
for number in range (1, 10):
   string = '{} x {} = {}'. format (단, number, 단 * number)
   print (string)
for 단 in range (2, 10):
    print ('{}단 시작'. format (단))
    for number in range (1, 10):
        string = '{} x {} = {}'. format (단, number, 단 * number)
        print (string)
    print ('{}단 종료'. format (단))
시작단 = int (input ('구구단 시작 단을 입력하세요 (1~9): '))
끝단= int (input ('구구단 끝 단을 입력하세요 (1~9): '))
for 단 in range (시작단, 끝단+1):
   for number in range (1, 10):
      string = '{} x {} = {}'. format (단, number, 단 * number)
      print (string)
for i in range (3, 7, 1):
   print (i)
for i in range (3, 7, 1):
   print (i)
   print ('--------')
while i <= 1000:
   print (i)
   i += 1
for i in range (1, 1001, 1):
   print (i)
for i in range (0, 1001, 3):
   print (i)
단 = 3
for number in range (1, 10):
   string = '{} x {} = {}'. format (단, number, 단 * number)
   print (string)
단 = 3
for number in range (1, 10, 2):
   string = '{} x {} = {}'. format (단, number, 단 * number)
   print (string)
