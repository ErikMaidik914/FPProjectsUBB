from src.repository.repo import Repository
from src.service.service import Service
from src.ui.ui import Ui

if __name__ == "__main__":
    repository = Repository()
    service = Service(repository)
    ui = Ui(service)
    ui.show_matrix()
    ui.menu()