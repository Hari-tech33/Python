class account:
    def __init__(self, holder_name, balance_):
        self.holder_name = holder_name
        self.balance_ = balance_

    def display_details(self):
        return f"Account Holder: {self.holder_name}, Balance: {self.balance_:.2f}"  
    
    def __add__(self, other):
        holder_name = self.holder_name + other.holder_name
        balance_ = self.balance_ + other.balance_
        return (holder_name, balance_)


class savings_account(account):

    def calculate_interest(self):
        return self.balance_ * 0.05
    
class current_account(account):

    def calculate_interest(self):
        return self.balance_ * 0.02

savings = savings_account("Ravi", 10000)
current = current_account("Anjali", 15000)

print(savings.display_details())
print("interest (5%):{savings.calculate_interest():}")

print(current.display_details())
print("interest (2%): {current.calculate_interest()}")

total_bal = savings + current
print(f"Total Balance of {savings.holder_name} and {current.holder_name}: {total_bal[1]:.2f}")

    

    

