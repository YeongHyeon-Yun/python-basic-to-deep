# 입력한 문자열에서 숫자, 영문 소문자, 영문 대문자, 한글, 기타 문자를 골라서 출력하는 프로그램을 작성하시오.
up = []
low = []
ko = []
digit = []
what =[]

string = input('\n문자열을 입력하세요 : ')
string = string.replace(' ', '')
for c in string:
    if c.isupper() == True:
        up.append(c)
    elif c.islower() == True:
        low.append(c)
    elif c.isalpha() == True:
        ko.append(c)
    elif c.isdigit() == True:
        digit.append(c)
    else:
        what.append(c)

print('대문자:',  ''.join(up))
print('소문자:', ''.join(low))
print('숫자:', ''.join(digit))
print('한글:', ''.join(ko))
print('기타:', ''.join(what))

############### 2번 째 방법 ###################
up = ""
low = ""
ko = ""
digit = ""
what = ""

string = input('\n문자열을 입력하세요 : ')
string = string.replace(' ', '')
for c in string:
    if c.isupper() == True:
        up += c
    elif c.islower() == True:
        low += c
    elif c.isalpha() == True:
        ko += c
    elif c.isdigit() == True:
        digit += c
    else:
        what += c

print('대문자:', up)
print('소문자:', low)
print('숫자:', digit)
print('한글:', ko)
print('기타:', what)