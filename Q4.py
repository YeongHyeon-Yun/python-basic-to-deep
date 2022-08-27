# 재귀 호출 함수를 이용해서 입력한 10진수를 2진수/8진수/16진수로 변환하는 코드를 작성하세요. 
# 재귀 호출 함수는 2진수로 변환하는 base2(숫자), 8진수로 변환하는 base8(숫자), 16진수로 변환하는 base16(숫자) 등 3개 함수를 작성하세요.

number = int(input('10진수 입력 --->'))
num_sixteen = ['A', 'B', 'C', 'D', 'E', 'F']

def base2(num):
    if num // 2 == 0:
        return str(num%2) + ' '
    return base2(num//2) + str(num%2) + ' '

def base8(num):
    if num // 8 == 0:
        return str(num%8) + ' '
    return base8(num//8) + str(num%8) + ' '

def base16(num):
    if num // 16 == 0:
        if num%16 < 10:
            return str(num%16) + ' '
        else:
            return str(num_sixteen[num%16 - 10]) + ' '

    else:
        if num%16 < 10:
            return base16(num//16) + str(num%16) + ' '
        else:
            return base16(num//16) + str(num_sixteen[num%16 - 10]) + ' '




print('2진수: ', base2(number))
print('8진수: ', base8(number))
print('16진수: ', base16(number))