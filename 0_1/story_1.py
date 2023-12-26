print ('당신은 호숫가에 서있습니다. 오른쪽 왼쪽 중 어느 길로 이동할까요?')
choice = input ('오른쪽 / 왼쪽 ')
if choice == '왼쪽':
    print ('예쁜 숲길이 나왔습니다. 계속 걸어갑니다.')
elif choice == '오른쪽':
    print ('한적한 오솔길이 나왔습니다. 계속 걸어갑니다.')
else:
    print ('이상한 선택을 하셔서 낭떠러지에서 떠러져서 죽었습니다.')
print ('한 동물이 눈에 띄었습니다. 어떤 동물인가요?')
animal = input ('동물: ')
print ('{}이/가 당신을 쳐다봅니다.'. format (animal))
print ('가지고 있슨 음식을 줍니다. 당신은 5개의 음식을 가지고 있습니다.')
n = int (input ('몇 개를 줄까요?'))
if n < 5:
    print ('{} : "배고파.더 줘. 더 있는거 알아."'. format (animal))
elif n > 5:
    print ('당신은 그만큼 줄 간식이 없습니다.')
else:
    i = 0
    while i < n:
        i = i + 1
        print ('{} : "냠냠. 마시따."'. format (animal))
print ('{} : 더줘!'. format (animal))
answer = input ('더 주시겠습니까? yes / no: ')
if answer == 'yes':
    print ('더 줄 수 있는 간식이 없습니다.')
if answer == 'no':
    print ('{}이/가 삐졌습니다.'. format (animal))
print ('{}이/가 선물을 요청합니다. 당신은 현제 공책, 팬, 지우개, 그리고 칼을 갖고 있습니다.'.format (animal) )
present = input ('무엇을 줄까요?: ')
if present == '공책':
    print ('{}이/가 공책이 간식인지 알고 먹어버렸습니다.'. format (animal))
    print ('{} : 앗! 갑자기... 배가.. 아프다!'. format (animal))
    print ('이런! {}이/가 배탈이 나서 죽어버렸습니다!'. format (animal))
elif present == '팬':
    print ('앗! 실수로 {}에게 떨어트려서 낙서를 해버렸내요!'. format (animal))
    print ('이런. {}이/가 단단히 화가 났네요! 망치를 들고 쫓아오고 있어요! 목숨을 아끼신다면 도망가세요!'. format (animal))
elif present == '지우개':
    print ('참 이런 실수도 다 있네요! 지우개로 실수로 {}를 지워버렸내요!'. format (animal))
    print ('{}이/가 사라졌어요!'. format (animal))
elif present == '칼':
    death = input ('칼을 손잡이 쪽으로 주나요, 아니면 칼날 쪽으로 주나요? 손잡이 / 칼날: ')
    if death == '손잡이':
        print ('{}이/가 당신을 칼로 찔러서 죽였습니다!'. format (animal))
        print ('게임을 다시 해보세요!')
    elif death == '칼날':
        print ('이런! 실수로 {}을/를 찔러서 죽여버렸내요!'. format (animal))
        print ('심지여 {}이/가 멸종위기종이였던거 있죠?'. format (animal))
        print ('경찰에게 체포당하기 전에 빨리 도망가세요!')
else:
    print ('이 물건은 현제 상황 갖고 있지 않은 물건 입니다.')
