import json

class JsonHandler:
    
    def save_group(self, group):
        
        data = {
            "group_name": group.group_name,
            
            "members": [member.name for member in group.members],
            
            "expenses":[
                {
                    "payer":expense.payer.name,
                    "amount":expense.amount,
                    "description":expense.description,
                    "participants":[participant.name for participant in expense.participants]
                }
                for expense in group.expenses
            ],
            
            "settlements":[
                {
                    "payer": settlement.payer.name,
                    
                    "receiver":settlement.receiver.name,
                    
                    "amount": settlement.amount
                }
                
                for settlement in group.settlements
            ]
        }
        
        with open("data\\data.json", "w") as file:
            json.dump(data,file,indent=4)
            
    def load_group(self):
        
        with open("data\\data.json", "r") as file:
            data = json.load(file)
            
        return data