from models.group import Group
from collections import defaultdict

class DebtCalculator:
    
    def calculate_debts(self, group):
        
        balances = defaultdict(float)
        
        for expense in group.expenses:
            
            balances[expense.payer.name] += expense.amount
            
            split_amount = expense.amount / len(expense.participants)
    
            for participant in expense.participants:
                
                balances[participant.name] -= split_amount
                
        for settlement in group.settlements:
            
            balances[settlement.payer.name] += settlement.amount
            
            balances[settlement.receiver.name] -= settlement.amount
                
        return balances
    
    def show_balances(self, balances):
        
        print("\n===== Current Balances =====")
        
        for name, amount in balances.items():
            
            if amount > 0:
                print(f"{name} should receive Rs.{amount:.2f}")
            
            elif amount < 0:
                print(f"{name} owes Rs.{abs(amount):.2f}")
            else:
                print(f"{name} is settled")