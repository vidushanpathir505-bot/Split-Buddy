import json

from models.group import Group
from models.user import User
from models.expense import Expense
from models.settlement import Settlement

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
        
        try:
            with open("data\\data.json", "w") as file:
                json.dump(data,file,indent=4)
        except FileNotFoundError:
            print(f"File Not Found!")
            
    def load_group(self):

        try:

            with open("data/data.json", "r") as file:

                content = file.read()

                if not content.strip():
                    return None, {}

                data = json.loads(content)

        except FileNotFoundError:

            print("file not found")
            return None, {}

        group = Group(
            data["group_name"]
        )

        users = {}

        for member_name in data["members"]:

            user = User(member_name)

            users[member_name] = user

            group.members.append(user)


        for expense_data in data["expenses"]:

            payer = users[
                expense_data["payer"]
            ]

            participants = [

                users[name]

                for name in expense_data[
                    "participants"
                ]
            ]

            expense = Expense(

                payer,
                expense_data["amount"],
                expense_data["description"],
                participants
            )

            group.expenses.append(
                expense
            )


        return group, users    
        
            
            