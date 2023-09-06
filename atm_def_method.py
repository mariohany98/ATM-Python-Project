import termcolor , pyfiglet
pin = '12345'
balance = 20000
withdraw_limit = 5000

def login(): 
    text = (pyfiglet.figlet_format('Enter your card'))
    print(termcolor.colored(text,'blue'))
    for i in range(3):
        global user_pin
        user_pin = input('enter your pin code\n')
        if user_pin == pin:
            print(termcolor.colored('welcome sir','green'))
            break
        elif i == 2:
            print(termcolor.colored('Invalid pin code please try again after 5 mins','red'))
        else:
            print(termcolor.colored('Invalid pin code please try again','yellow'))

def checkbalance():
    print(termcolor.colored(f'your balance is {balance}EGB','green'))

def withdraw():
    print(termcolor.colored('choose how much money do you want to withdraw','green'))
    amount = int(input('100          200\n300          500\n1000         2000\n'))
    global balance , withdraw_limit
    if amount <= balance and amount <= withdraw_limit:
        balance = balance - amount
        withdraw_limit = withdraw_limit - amount
        print(termcolor.colored('please take your money','green'))
    elif amount > balance:
        print(termcolor.colored('sorry your balance does not have enough money','yellow'))
    elif amount > withdraw_limit:
        if withdraw_limit > 0:
            print(termcolor.colored(f'you can not withdraw more than {withdraw_limit} EGB','red'))
        elif withdraw_limit == 0:
            print(termcolor.colored(f'you have reached the maximum withdraw limit of today','red'))

def logout():
    print(termcolor.colored('you have logged out successfully please take your card','green'))

def atm():
    login()
    if user_pin == pin:
        while True:
            ask =input('1-check balance\n2-withdraw\n3-logout\n')
            if ask == '1':
                checkbalance()
            elif ask == '2':
                withdraw()
            elif ask == '3':
                logout()
                break
            else:
                print(termcolor.colored('invalid choice please try again','red'))
atm()