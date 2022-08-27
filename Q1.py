# ‘가위’ , ‘바위’ , ‘보’  를 사용자에게 입력받고, 컴퓨터는 난수를 생성하여 승패를 출력한다. 
# 사용자가 연속으로 이길 때마다 연승 횟수가 올라가며 컴퓨터가 이겼을 때 연승횟수를 출력하고 게임을 종료한다.

import random

option = ['가위', '바위', '보']

count=0
user_vic=0
user_next_vic=0
flag = 0

print('\n가위,바위,보 게임을 시작합니다.')

while True:
    user_hand = input('\n입력: ')
    if user_hand not in option:
        print('좋은 말로 할 때 다시 입력해주세요')
        continue
    com_hand = random.choice(option)

    if user_hand == option[0]:
        if com_hand == option[0]:
            print(f'컴퓨터: {com_hand} 플레이어: {user_hand} 비김')
            count += 1
            flag = 1
        elif com_hand == option[1]:
            print(f'컴퓨터: {com_hand} 플레이어: {user_hand} 패배')
            count += 1
            print('패배로 인한 게임 종료\n')
            print('결과')
            print(f'게임수: {count}회 승리: {user_vic}회 연승: {user_next_vic}회')
            break
        elif com_hand == option[2]:
            print(f'컴퓨터: {com_hand} 플레이어: {user_hand} 승리')
            count += 1
            user_vic += 1
            if flag == 0:
                user_next_vic += 1
            flag = 0
    
    if user_hand == option[1]:
        if com_hand == option[1]:
            print(f'컴퓨터: {com_hand} 플레이어: {user_hand} 비김')
            count += 1
            flag = 1
        elif com_hand == option[2]:
            print(f'컴퓨터: {com_hand} 플레이어: {user_hand} 패배')
            count += 1
            print('패배로 인한 게임 종료\n')
            print('결과')
            print(f'게임수: {count}회 승리: {user_vic}회 연승: {user_next_vic}회')
            break
        elif com_hand == option[0]:
            print(f'컴퓨터: {com_hand} 플레이어: {user_hand} 승리')
            count += 1
            user_vic += 1
            if flag == 0:
                user_next_vic += 1
            flag = 0

    if user_hand == option[2]:
        if com_hand == option[2]:
            print(f'컴퓨터: {com_hand} 플레이어: {user_hand} 비김')
            count += 1
            flag = 1
        elif com_hand == option[0]:
            print(f'컴퓨터: {com_hand} 플레이어: {user_hand} 패배')
            count += 1
            print('패배로 인한 게임 종료\n')
            print('결과')
            print(f'게임수: {count}회 승리: {user_vic}회 연승: {user_next_vic}회')
            break
        elif com_hand == option[1]:
            print(f'컴퓨터: {com_hand} 플레이어: {user_hand} 승리')
            count += 1
            user_vic += 1
            if flag == 0:
                user_next_vic += 1
            flag = 0

    