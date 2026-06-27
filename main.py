from models.user import User
from models.group import Group
from models.expense import Expense

from services.expense_manager import ExpenseManager
#from services.debt_calculator import DebtCalculator

kasun = User("Kasun")
amara = User("Amara")
nayana = User("Nayana")

expense1 = Expense(kasun, 1000, "Dinner", [kasun, amara, nayana])

bodima = Group("Bodima")
bodima.add_members(kasun)
bodima.add_members(amara)
bodima.add_members(nayana)
bodima.add_expense(expense=expense1)

expense2 = Expense(amara, 2000, "Bus Money", [kasun, amara, nayana])
bodima.add_expense(expense=expense2)

exp = ExpenseManager()

exp.show_expenses(bodima)

print(bodima.expenses)

exp.remove_expense(bodima, expense2)

exp.show_expenses(bodima)