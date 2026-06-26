import json

class JaonHandler:
    
    def save_group(self, group):
        
        data = {
            "group_name": group.group_name,
            
            "members": [member.name for member in group.members],
            
            "expenses":[
                {
                    "payer":expense.payer,
                    "amount":expense.amount,
                    "description":expense.discription,
                    "participants":expense.participants
                }
                for expense in group.expenses
            ]
        }
        
        with open("data\data.json", "w") as file:
            json.dump(data,file,indent=4)
            
    def load_group(self):
        
        with open("data\data.json", "r") as file:
            data = json.load(file)
            
        return data