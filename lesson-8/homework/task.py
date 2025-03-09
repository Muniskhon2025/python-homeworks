# Farm Model

class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}!")
    
    def eat(self, food):
        print(f"{self.name} is eating {food}.")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow", "Moo")
    
    def produce_milk(self):
        print(f"{self.name} is producing milk.")

class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken", "Cluck")
    
    def lay_egg(self):
        print(f"{self.name} laid an egg.")

class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "Sheep", "Baa")
    
    def shear_wool(self):
        print(f"{self.name} has been sheared for wool.")

# Example Usage
bessie = Cow("Bessie")
bessie.make_sound()
bessie.eat("grass")
bessie.produce_milk()

clucky = Chicken("Clucky")
clucky.make_sound()
clucky.eat("corn")
clucky.lay_egg()

wooly = Sheep("Wooly")
wooly.make_sound()
wooly.eat("hay")
wooly.shear_wool()


# Bank Application
import json

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")
    
    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        print(f"Account created: {account_number}, Name: {name}, Balance: {initial_deposit}")
        self.save_to_file()
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account: {account.account_number}, Name: {account.name}, Balance: {account.balance}")
        else:
            print("Account not found.")
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")
    
    def save_to_file(self):
        with open("accounts.txt", "w") as f:
            json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, f)
    
    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as f:
                data = json.load(f)
                self.accounts = {int(acc_num): Account(**details) for acc_num, details in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}

# Example Usage
bank = Bank()
bank.create_account("Alice", 500)
bank.create_account("Bob", 1000)
bank.view_account(1)
bank.deposit(1, 200)
bank.withdraw(2, 500)
