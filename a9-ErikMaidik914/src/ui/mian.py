from src.ui.ui import Console
from src.repository.repository import Repository
from src.controller.controller import Controller




if __name__ == '__main__':
    repo = Repository()
    controller = Controller(repo)
    console = Console(controller)
    console.menu()
