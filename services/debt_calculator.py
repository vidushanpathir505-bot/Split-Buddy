from models.group import Group
import math
from collections import defaultdict

class DebtCalculator:
    
    def calculate_debts(self, group):
        
        balance = defaultdict(float)
        
        for expense in group.expenses:
            
            balance[expense.payer.name] += expense.amount
            
            split_amount = expense.amount / len(expense.participants)
    
            for person in expense.participants:
                
                balance[person.name] -= split_amount
                
        return balance