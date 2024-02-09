from client import Client
from uuid import uuid4
class Account():
    def __init__(self, Client) -> None:
        self.client = Client
        self.account = str(f'{uuid4}-0001')
        self.amount = 0
        
    def deposit(self,value):
        self.amount.append(value)

    def withdrawl(self,value, account):
        withdraws = 0
        
        if value < 0.0:
            print("The value is negative")
        elif value >= 500.00:
            print("Sorry, you can't withdrawl this amount")
        elif sum(account) <=  value:
            print("You don't have enough money on your account")
        else:
            self.amount.append(-value)
            
    def bank_statement(account):
        if not account:
            return("No bank transactions were made.")
        else:
            total_balance = sum(account)
            return(f'Your bank balance is ${total_balance:.2f}')
