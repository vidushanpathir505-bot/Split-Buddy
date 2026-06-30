class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []
        self.expenses = []
        self.settlements = []
        
    def add_members(self, user):
        self.members.append(user)
        
    def add_expense(self, expense):
        self.expenses.append(expense)
        