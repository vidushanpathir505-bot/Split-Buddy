from models.user import User
from models.group import Group
from models.expense import Expense

from services.expense_manager import ExpenseManager
from services.debt_calculator import DebtCalculator
from storage.json_handler import JsonHandler


def display_menu():
    
    print("\n========== SPLIT-BUDDY ==========")
    print("1. Create/Select Group")
    print("2. Add Member to Group")
    print("3. View Group Members")
    print("4. Add Expense")
    print("5. View All Expenses")
    print("6. View User Expenses")
    print("7. Calculate Debts")
    print("8. Settle Payment")
    print("9. Remove Expense")
    print("10. Remove Member")
    print("11. Exit")
    print("================================\n")


def main():
    
    # Initialize services and storage
    expense_manager = ExpenseManager()
    debt_calculator = DebtCalculator()
    json_handler = JsonHandler()
    
    group, users = json_handler.load_group()
    
    if group:
        print(f"Loaded previous group: {group.group_name}")
    else:
        print("No previous data found.")
    
    print("Welcome to SPLIT-BUDDY!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ").strip()
        
        if choice == "1":
            # Create or select group
            if group:
                print(f"Already in group: {group.group_name}")
            else:
                group_name = input("Enter group name: ").strip()
                group = Group(group_name)
                print(f"Group '{group_name}' created successfully!\n")
        
        elif choice == "2":
            # Add member to group
            if not group:
                print("Please create a group first!")
                continue
            
            member_name = input("Enter member name: ").strip()
            if member_name in users:
                user = users[member_name]
            else:
                user = User(member_name)
                users[member_name] = user
            
            expense_manager.add_member(group, user)
        
        elif choice == "3":
            # View group members
            if not group:
                print("Please create a group first!")
                continue
            
            print(f"\n--- Members in {group.group_name} ---")
            expense_manager.show_members(group)
        
        elif choice == "4":
            # Add expense
            if not group:
                print("Please create a group first!")
                continue
            
            if not group.members:
                print("Please add members to the group first!")
                continue
            
            payer_name = input("Who paid? (Enter member name): ").strip()
            
            # Find payer in group members
            payer = next((m for m in group.members if m.name == payer_name), None)
            if not payer:
                print("Payer not found in group members!")
                continue
            
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount! Please enter a number.")
                continue
            
            description = input("Enter expense description: ").strip()
            
            # Select participants
            print("Select participants (enter names separated by comma):")
            expense_manager.show_members(group)
            participants_input = input("Participant names: ").strip().split(",")
            
            participants = []
            for name in participants_input:
                name = name.strip()
                participant = next((m for m in group.members if m.name == name), None)
                if participant:
                    participants.append(participant)
            
            if not participants:
                print("No valid participants selected!")
                continue
            
            expense = Expense(payer, amount, description, participants)
            expense_manager.add_expense(group, expense)
        
        elif choice == "5":
            # View all expenses
            if not group:
                print("Please create a group first!")
                continue
            
            print(f"\n--- All Expenses in {group.group_name} ---")
            expense_manager.show_expenses(group)
        
        elif choice == "6":
            # View user expenses
            if not group:
                print("Please create a group first!")
                continue
            
            if not group.members:
                print("No members in group!")
                continue
            
            user_name = input("Enter member name: ").strip()
            user = next((m for m in group.members if m.name == user_name), None)
            
            if not user:
                print("Member not found!")
                continue
            
            print(f"\n--- Expenses by {user_name} ---")
            expense_manager.show_user_expense(user, group)
        
        elif choice == "7":
            # Calculate and show debts
            if not group:
                print("Please create a group first!")
                continue
            
            balances = debt_calculator.calculate_debts(group)
            debt_calculator.show_balances(balances)
        
        elif choice == "8":
            # Settle payment
            if not group:
                print("Please create a group first!")
                continue
            
            if not group.members:
                print("No members in group!")
                continue
            
            print("Who is paying?")
            expense_manager.show_members(group)
            payer_name = input("Enter payer name: ").strip()
            payer = next((m for m in group.members if m.name == payer_name), None)
            
            if not payer:
                print("Payer not found!")
                continue
            
            print("Who is receiving?")
            receiver_name = input("Enter receiver name: ").strip()
            receiver = next((m for m in group.members if m.name == receiver_name), None)
            
            if not receiver:
                print("Receiver not found!")
                continue
            
            try:
                amount = float(input("Enter settlement amount: "))
            except ValueError:
                print("Invalid amount!")
                continue
            
            expense_manager.settle_payment(group, payer, receiver, amount)
        
        elif choice == "9":
            # Remove expense
            if not group:
                print("Please create a group first!")
                continue
            
            description = input("Enter expense description to remove: ").strip()
            expense = expense_manager.find_expense(group, description)
            
            if expense:
                expense_manager.remove_expense(group, expense)
            else:
                print("Expense not found!")
        
        elif choice == "10":
            # Remove member
            if not group:
                print("Please create a group first!")
                continue
            
            member_name = input("Enter member name to remove: ").strip()
            member = next((m for m in group.members if m.name == member_name), None)
            
            if member:
                expense_manager.remove_member(group, member)
            else:
                print("Member not found!")
        
        elif choice == "11":
            # Exit
            if group:
                json_handler.save_group(group)
             
            print("\nData saved.")   
            print("\nThank you for using SPLIT-BUDDY!")
            print("Goodbye!\n")
            break
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()




