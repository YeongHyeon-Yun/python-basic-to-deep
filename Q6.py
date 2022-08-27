# 계좌 정보를 입력받아 계좌를 관리하는 프로그램을 아래 예제를 참조하여 작성하시오

class BankAccount:
    account_list = []
    def __init__(self):
        pass
    def setting(self, acc_num, user, money):
        self.acc_num = acc_num
        self.user = user
        self.money = money
        return print('결과: 계좌가 생성되었습니다.')

    def deposit(self, money):
        self.money += money
        return print('결과: 예금이 성공되었습니다.')

    def withdraw(self, money):
        if self.money >= money:
            self.money -= money
        else:
            return print('결과: 잔액이 부족합니다.')
    
    def show_info(self):
        return print(f'{self.acc_num}      {self.user}     {self.money}')
    
    @classmethod
    def make_account(cls):
        pass


while True:
    print('------------------------------------------------------------')
    print('1.계좌생성 | 2.계좌목록 | 3.예금 | 4. 출금 | 5.종료')
    print('------------------------------------------------------------')
    user_input = int(input('선택> '))
    
    if user_input == 1:
        print('-------------')
        print('계좌생성')
        print('-------------')
        acc_num = input('계좌번호: ')
        user = input('계좌주: ')
        money = int(input('초기입금액: '))
        temp = acc_num
        temp = BankAccount()
        temp.setting(acc_num, user, money)
    
    elif user_input == 2:
        print('-------------')
        print('계좌목록')
        print('-------------')
        temp.show_info()

    elif user_input == 3:
        print('-------------')
        print('예금')
        print('-------------')
        acc_num = input('계좌번호: ')
        temp.deposit(int(input('예금액: ')))

    elif user_input == 4:
        print('-------------')
        print('출금')
        print('-------------')
        acc_num = input('계좌번호: ')
        temp.withdraw(int(input('출금액: ')))
        

    elif user_input == 5:
        print('프로그램 종료')
        break