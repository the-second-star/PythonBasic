import random
foods = ['김치 볶음밥', '봉골레 파스타', '페퍼로니 피자', '감자튀김', '라구 파스타', '돈코츠 라멘', '김치찌게', '우동', '프링글스', '꼬깔콘', '라볶이', '라면', '떡볶이']
title = '''1. 메뉴 추가
2. 메뉴 삭제
3. 메뉴 출력
4. 메뉴 추천
5. 종료'''
while True:
    print ("\n{}". format (title))
    command = input ("\n{}". format ('어떤 작업을 하시겠습니까? '))
    if command == '1':
        food = input ('추가할 메뉴: ')
        foods. append (food)
    elif command == '2':
        food = input ('삭제할 메뉴: ')
        foods. remove (food)
    elif command == '3':
        for food in foods:
            print ("\n{}". format (food))
    elif command == '4':
        pick = random. choice (foods)
        print ("\n{}".format (pick))
    elif command == '5':
        break
