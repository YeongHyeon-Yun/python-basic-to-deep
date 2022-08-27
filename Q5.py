# 주사위 게임을 만드시오 주사위 게임은 주사위를 던져서 높은 숫자가 나오면 이기는 게임이다.  
# 컴퓨터와 주사위 게임을 n번 하여 사람이 이긴 횟수와 플래이한 경기 내용을 기록하여 출력 하시오. 
# 출력 결과는 n번의 경기 내용과 경기 결과, 플래이어가 컴퓨터를 이긴 횟수, 비긴 횟수, 진 횟수를 각각 출력하시오.

import random
import numpy as np


gametime = int(input('\n게임횟수를 입력하시오: '))
print('-------------------------------------------')
print(f'게임을 {gametime}회 시작합니다.')

recode = np.arange(gametime * 3).reshape(gametime, 3)

for i in range(gametime):
    computer = random.randrange(1, 7)
    user = random.randrange(1, 7)
    print('-------------------------------------------')
    print(f'{i+1}회차')
    print('컴퓨터 :', computer)
    input('주사위를 굴리시오 (엔터입력)')
    print('플래이어 :', user)
    print('-------------------------------------------')
    
    recode[i] = [i+1, user, computer]

print(f'결과 \n {gametime}번 경기내용')
win = 0
draw = 0
lose = 0 

for i in range(gametime):
    print(f'{recode[i][0]}회차 - 플래이어: {recode[i][1]}, 컴퓨터: {recode[i][2]}', end=' ')

    if recode[i][1] == recode[i][2]:
        print('비김')
        draw += 1
    elif recode[i][1] > recode[i][2]:
        print('승리')
        win += 1
    elif recode[i][1] < recode[i][2]:
        print('패배')
        lose += 1

print('-------------------------------------------')
print(f'게임수: {gametime}회, 승리: {win}회, 비김: {draw}, 패배: {lose}회')
print('-------------------------------------------')