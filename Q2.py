# 사용자가 입력한 문자가 소문자면 대문자로, 대문자면 소문자로 바꾸어 출력하는 프로그램을 만드시오.
# 알파벳 이외의 값이 들어오면 프로그램이 종료.

exit = 0
while True:
    string = input('\n입력: ')
    for c in string:
        if (c == ' ') or (c.isalpha() == True):
            pass
        else:
            string = string.replace(c, '')
            exit = 1

    string = string.swapcase()
    print(string)
    if exit == 1:
        break