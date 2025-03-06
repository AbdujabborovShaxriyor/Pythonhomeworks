#Account class

class Account:
    
    #constuctor
    
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name=name
        if balance>=0:
            self.balance = balance
    
class Bank:
      
    def __init__(self,filename="bank.txt"):
        self.accounts={}
        self.filename = filename
        self.load_accounts()
        
    #loading
    
    def load_accounts(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.strip().split(" | ")  # Split by separator
                    if len(parts) == 3:  # Ensure correct format
                        account_number = int(parts[0])
                        name = parts[1]
                        balance = float(parts[2])
                        self.accounts[account_number] = Account(account_number, name, balance)
        except FileNotFoundError:
            print("No existing accounts found, starting fresh.")
    
    #saving
    
    def save_accounts(self):
        with open(self.filename,"w") as file:
            for account in self.accounts.values():
                file.write(f"{account.account_number} | {account.name} | {account.balance}\n")    
    
    #create account
    
    def create_account(self,name, initial_deposit)->Account:
        account_number = len(self.accounts)+1
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number]=new_account
        print("Account created successfully")
        return new_account
    
    #view account
    
    def view_account(self, account_number):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            print(f"Account({acc.account_number}, {acc.name}, {acc.balance})")
        else:
            print("Account not found!")
    
    #deposit
    
    def deposit(self,account_number, amount):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            if amount>0:
                acc.balance+=amount
    
    #withdraw
    
    def withdraw(self,account_number, amount):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            if acc.balance>=amount and amount>0:
                acc.balance-=amount
                
    
            
    
        