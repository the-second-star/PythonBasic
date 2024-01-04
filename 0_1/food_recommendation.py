import random
foods = ['김치 볶음밥', '봉골레 파스타', '페퍼로니 피자', '감자튀김', '라구 파스타', '돈코츠 라멘', '김치찌게', '우동', '프링글스', '꼬깔콘', '라볶이', '라면', '떡볶이']
print ('추천 가능한 음식')
print ('=' * 50)
for food in foods:
    print (food)
print ('=' * 50)
while True:
    pick = random.choice (foods)
    print (pick)
    user = input ('다시 추천을 받으시겠습니까(네 / 아니요)? ')
    if user == '아니요':
        break
