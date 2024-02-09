import sys
import time
from client import Client 
from account import Account

USER_LIST= []

def create_user(first_name, last_name, birthdate, cpf, address):
    if any(client.cpf == cpf for client in USER_LIST):
        return 'User already created'
    
    new_user = Client(first_name, last_name, birthdate, cpf, address)
    USER_LIST.append(new_user)
    print()
    print('==================================')
    print('Your user is: ')
    for key, value in new_user.__dict__.items():
        print(f'{key}: {value}')
    
    print('User created')
    return new_user

def create_account(user):
    client = Account(user)
    return client


def deposit(value):
    ACCOUNT.append(value)

def withdrawl(value, account):
    withdraws = 0
    
    if value < 0.0:
        print('=====================')
        print("The value is negative")
    elif value >= 500.00:
        print('=====================')
        print("Sorry, you can't withdrawl this amount")
    elif sum(account) <=  value:
        print('=====================')
        print("You don't have enough money on your account")
    else:
        ACCOUNT.append(-value)
         
def bank_statement(account):
    if not account:
        print('=====================')
        return("No bank transactions were made.")
    else:
        total_balance = sum(account)
        print('=====================')
        return(f'Your bank balance is ${total_balance:.2f}')

INPUT_MENU = """
                1 - Login
                2 - Create Account

            """

def main_menu():
    while True:
        print("          Bank CLI           ")
        print(MENU)
        option = input()
        
        match option:
            case "1":
                print(bank_statement(ACCOUNT))
            case "2":
                print('=====================')
                print("deposit")
                print('=====================')
                print("How much you want to deposit?")
                value = float(input())
                deposit(value)
                print(bank_statement(ACCOUNT))
            case "3":
                print('=====================')
                print("WithDrawl")
                withdraws += 1
                if withdraws > 3:
                    print('=====================')
                    print("You have reached the withdrawl limit today!")
                    break
                print(withdraws)
                print('=====================')
                print("how much you want to withdraw?")
                value = float(input())
                withdrawl(value, ACCOUNT)
                print(bank_statement(ACCOUNT))
                
            case "4":
                print('=====================')
                print("Goodbye!")
                break
            case _:
                print('=====================')
                print("Invalid option. Please try again.")


ACCOUNT = []
MENU = """
        1 - bank statement
        2 - deposit
        3 - withdrawl
        4 - exit
       """
       
       


withdraws = 0
if __name__ == "__main__":
    
        print("          Bank CLI           ")
        print(INPUT_MENU)
        option = input()
        match option:
            case '1':
                print('Insert your CPF ----> ')
                cpf = input()
                if cpf in USER_LIST:
                    main_menu()
                else:
                    first_name = input('Fist Name ')
                    last_name = input('Last Name ')
                    birthdate = input('Birthdate ')
                    address = input('Address ')
                    create_user(cpf = cpf, first_name= first_name, last_name=last_name, birthdate= birthdate, address= address)
                    main_menu()
            case '2':
                pass
            
            case _:
                sys.out(0)
        
        