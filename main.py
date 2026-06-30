from models.user import User
from models.group import Group
from models.expense import Expense

from services.expense_manager import ExpenseManager
from services.debt_calculator import DebtCalculator

exp = ExpenseManager()
debt = DebtCalculator()

kasun = User("Kasun")
amara = User("Amara")
nayana = User("Nayana")

expense1 = Expense(kasun, 1000, "Dinner", [kasun, amara, nayana])

bodima = Group("bodima")
bodima.add_members(kasun)
bodima.add_members(amara)
bodima.add_members(nayana)
bodima.add_expense(expense=expense1)

expense2 = Expense(amara, 2000, "Bus Money", [kasun, amara, nayana])

expense3 = Expense(nayana, 1500, "groccery shop", [kasun, amara, nayana])

expense4 = Expense(amara, 400, "Party", [kasun, amara, nayana])
bodima.add_expense(expense=expense2)

exp.show_expenses(bodima)

exp.add_expense(bodima, expense=expense3)

exp.add_expense(bodima, expense=expense4)

#exp.remove_expense(bodima, expense2)

exp.show_members(bodima)

exp.show_expenses(bodima)

print(exp.total_expense(bodima))

exp.show_user_expense(amara, bodima)

print(debt.calculate_debts(bodima))