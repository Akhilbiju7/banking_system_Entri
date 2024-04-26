class BankAccount:
    def __init__(self,account_number,pin,balance=0):
        self.account_number=account_number
        self.pin=pin
        self.balance=balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited ${amount}. new balance${self.balance}")
        else:
            print("invalid amount to deposit")
            
    def withdraw(self,amount):
        if amount>0:
            if amount<self.balance:
                self.balance-=amount
                print(f"withdraw ${amount}. New balance ${self.balance}")
            else:
                print("insuffiant balance to withdraw")
        else:
            print("invalid amount for withdraw")
            
def create_account():
    account_number=input("Enter your account number")
    pin=input("Enter your pin")
    return BankAccount(account_number, pin)
    
 
def main():
    accounts={}
    while True:
        print("\n1.Log in")
        print("2.create acoount")
        print("3.exit")
        option=input("Enter your choice")
        
        if option=='1':
            account_number=input("Enter your account number")
            pin=input("Enter your pin")
            if account_number in accounts and accounts[account_number].pin==pin:
                print("Login successfully")
                current_account=accounts[account_number]
                account_menu(current_account)
            else:
                print("invalid account number or pin")
        elif option=='2':
            new_account=create_account()
            accounts[new_account.account_number]=new_account
            print("Account created successfully")
        elif option=='3':
            print("Thank y ou for usng our bank")
            break
        else:
            print("invalid option number")
            
def account_menu(account):
    while True:
        print("1.deposit")
        print("2.withdraw")
        print("3.logout")
        option=input("Enter your choice")
        if option=='1':
            amount=float(input("enter amount to be deposited"))
            account.deposit(amount)
        elif option=='2':
            amount=float(input("enter amount for withdraw"))
            account.withdraw(amount)
        elif option=='3':
            print("loged out succesfully")
            break
        else:
            print("invalid option number")
            
main()
            
            
            
            
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            