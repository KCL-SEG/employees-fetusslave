"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def get_pay(self):
        return self.pay.get_total()

    def __str__(self):
        return f"{self.name} {self.pay.__str__()}. Their total pay is {self.get_pay()}."

class Pay:
    def __init__(self):
        pass
    def get_total(self):
        return 0

class Salary(Pay):
    def __init__(self, salary):
        super().__init__()
        self.salary = salary
    def get_total(self):
        return self.salary
    def __str__(self):
        return f"works on a monthly salary of {self.salary}"

class Hourly(Pay):
    def __init__(self, contract_length, salary):
        super().__init__()
        self.contract_length = contract_length
        self.salary = salary
    def get_total(self):
        return self.contract_length*self.salary
    def __str__(self):
        return f"works on a contract of {self.contract_length} hours at {self.salary}/hour"

class Commission:
    def __init__(self, base_pay):
        self.base_pay = base_pay
    def get_total():
        return 0

class BonusCommission(Commission):
    def __init__(self, base_pay, amount):
        super().__init__(base_pay)
        self.amount = amount
    def get_total(self):
        return self.base_pay.get_total()+self.amount
    def __str__(self) -> str:
        return self.base_pay.__str__()+f" and receives a bonus commission of {self.amount}"

class ContractCommission(Commission):
    def __init__(self, base_pay, contracts, amount):
        super().__init__(base_pay)
        self.contracts = contracts
        self.amount = amount
    def get_total(self):
        return self.base_pay.get_total()+self.contracts*self.amount
    def __str__(self):
        return self.base_pay.__str__()+f" and receives a commission for {self.contracts} contract(s) at {self.amount}/contract"
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Salary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Hourly(100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', ContractCommission(Salary(3000), 4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', ContractCommission(Hourly(150, 25), 3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', BonusCommission(Salary(2000), 1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', BonusCommission(Hourly(120, 30), 600))
