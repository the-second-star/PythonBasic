import random
win = 0
com_win = 0
print ('이 게임은 가위 바위 보 게임 입니다. 중단 하시고 싶을 시 "그만" 을 입력해주세요.')
while True:
    com = random. randint(1, 3)
    if com == 1:
     com = '가위'
    elif com == 2:
     com = '바위'
    elif com == 3:
     com = '보'
    player = input ('가위, 바위 , 보 중 어떤 것을 선택 하겠습니까?: ')
    print ('사용자 ({} vs {}) 컴퓨터'. format (player, com))
    if player == '그만':
        print ('가위 바위 보 게임이 중단 되었습니다.')
        if win > com_win:
            print ('사용자 최종 승리')
            break
        if win < com_win:
            print ('컴퓨터 최종 승리')
            break
        if win == com_win:
            print ('최종 무승부')
            break
    if com == '가위':
        if player == '가위':
            print ('무승부')
        elif player == '바위':
            print ('사용자 승, 컴퓨터 패')
            win = win + 1
        elif player == '보':
            print ('컴퓨터 승, 사용자 패')
            com_win = com_win + 1
    elif com == '바위':
        if player == '가위':
            print ('컴퓨터 승, 사용자 패')
            com_win = com_win + 1
        elif player == '바위':
            print ('무승부')
        elif player == '보':
            print ('사용자 승, 컴퓨터 패')
            win = win + 1
    elif com == '보':
        if player == '가위':
            print ('사용자 승, 컴퓨터 패')
            win = win + 1
        elif player == '바위':
            print ('컴퓨터 승, 사용자 패')
            com_win = com_win + 1
        elif player == '보':
            print ('무승부')
    
