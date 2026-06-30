from models.settlement import Settlement

class ExpenseManager:

    def show_expenses(self, group):
        
        if not group.expenses:
            print("No expenses available")
            return
        
        for expense in group.expenses:
            print(f"{expense.payer.name} paid Rs.{expense.amount} for {expense.description}")
            
    def remove_expense(self, group, expense):
        
        if expense in group.expenses:
            group.expenses.remove(expense)
            print("Delete Successful")
        
        else:
            print("Expense is not Found")
            
    def add_expense(self, group, expense):
        
        if expense.amount <= 0:
            print("Invalid amount")
            return
        
        if expense.payer not in group.members:
            print("Payer not in group")
            return
        
        group.expenses.append(expense)
        
        print("Expense add Successful")
        
    def show_members(self, group):
        
        if not group.members:
            print("No Members in Group")
            return
        
        for member in group.members:
            print(member.name)
        
    def add_member(self, group, user):
        
        if user not in group.members:
            group.members.append(user)
            print("Member added")
            
    def remove_member(self, group, user):
        
        if user in group.members:
            group.members.remove(user)
            print("Member Remove")
            
    def find_expense(self, group, description):
        
        return next((e for e in group.expenses if e.description == description), None)
    
    def total_expense(self, group):
        
        total = 0
        
        for expense in group.expenses:
            total += expense.amount
            
        return total
    
    def show_user_expense(self, user, group):
        
        if not group.expenses:
            print("No expenses available")
            return
        
        total = 0
        
        for expense in group.expenses:
            if expense.payer == user:
                total += expense.amount
                print(f"{expense.description} | Rs.{expense.amount}")
        
        print(f"Total Expenses | {total}")
        
    def settle_payment(self, group, payer, receiver, amount):
        
        if amount <= 0:
            print("Invalid Amount")
            return
        
        settlement = Settlement(payer, receiver, amount)
        
        group.settlements.append(settlement)
        
        print("Payment settled successfully")
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
    
        