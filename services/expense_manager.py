from models.expense import Expense
from models.group import Group


class ExpenseManager:
    
    def __init__(self):
        pass
    
    def show_expenses(self, group):
        
        for expense in group.expenses:
            print(f"{expense.payer.name} paid Rs.{expense.amount} for {expense.description}")
            
    def remove_expense(self, group, expense):
        
        if expense in group.expenses:
            group.expenses.remove(expense)
            print("Delete Successful")
        
        else:
            print("Expense is not Found")