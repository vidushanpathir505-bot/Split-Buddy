from models.expense import Expense
from models.group import Group
from storage.json_handler import JsonHandler

class ExpenseManager:
    
    def __init__(self):
        self.json_handler = JsonHandler()
    
    def show_expences(self, group):
        
        for expense in group.expences:
            print(f"{expense.payer} paid Rs.{expense.amount}")
            
    