import os

from src.repository.binary_file_repository import BinaryRepository
from src.repository.file_repository import FileRepository
from src.domain.entities import Expense
from src.repository.expense_repo import ExpenseRepository
from src.services.expense_service import ExpenseService
from src.ui.ui import Console

if __name__ == '__main__':
    # expense_repo = ExpenseRepository()
    #file = 'expenses.txt'
    #expense_repo = FileRepository(file)
    file = 'expenses.bin'
    expense_repo = BinaryRepository(file)
    expense_service = ExpenseService(expense_repo)
    console = Console(expense_service)
    console.menu()
