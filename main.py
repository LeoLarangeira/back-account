import time


def deposit(value):
    ACCOUNT.append(value)

def withdrawl(value, account):
    withdraws = 0
    
    if value < 0.0:
        print("The value is negative")
    elif value >= 500.00:
        print("Sorry, you can't withdrawl this amount")
    elif sum(account) <=  value:
        print("You don't have enough money on your account")
    else:
        ACCOUNT.append(-value)
         
def bank_statement(account):
    if not account:
        return("No bank transactions were made.")
    else:
        total_balance = sum(account)
        return(f'Your bank balance is ${total_balance:.2f}')

ACCOUNT = []
MENU = """
        1 - bank statement
        2 - deposit
        3 - withdrawl
        4 - exit
       """


withdraws = 0
if __name__ == "__main__":
    
    while True:
        print("          Bank CLI           ")
        print(MENU)
        option = input()
        
        match option:
            case "1":
                print(bank_statement(ACCOUNT))
            case "2":
                print("deposit")
                
                print("How much you want to deposit?")
                value = float(input())
                deposit(value)
                print(bank_statement(ACCOUNT))
            case "3":
                print("WithDrawl")
                withdraws += 1
                if withdraws > 3:
                    print("You have reached the withdrawl limit today!")
                
                print(withdraws)
                print("how much you want to withdraw?")
                value = float(input())
                withdrawl(value, ACCOUNT)
                print(bank_statement(ACCOUNT))
                
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")