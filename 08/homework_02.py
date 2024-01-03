books = ['모모', '어린왕자', '별', '돈키호테', '마당을 나온 암탉']
books. append ('percy jackson')
books. insert (1, '데미안')
del books [3]
books. remove ('돈키호테')
print (books)
family = [] 
while True:
    name = input("가족 구성원의 이름 : ")
    if name == '끝' :
        break 
    family. append (name)
print (family)
foods = []
while True: 
    food = input ("좋아하는 음식은 무엇입니까? ")
    if food == '끝':
        break
    foods. append (food) 
print (foods)
movies = ('보스베이비', '어벤져스')
# movies[0] = '슈퍼배드' : 실행 불가능
# movies. append('겨울왕국') : 실행 불가능
# print(movies[2]) : 실행 불가능
# del movies[0] : 실행 불가능
print(movies[0])
grade = ('A등급', 'B등급', 'C등급', 'D등급', 'E등급')
score = int (input ("점수: "))
if score > 81:
    print (grade [0])
elif score > 61:
    print (grade [1])
elif score > 41:
    print (grade [2])
elif score > 21:
    print (grade [3])
else:
    print (grade [4])
