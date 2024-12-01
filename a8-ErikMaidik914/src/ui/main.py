from src.domain.entities import Person
from src.domain.entities import Activity
from src.repository.pers_repo import PersonRepo
from src.services.pers_service import Pers_service
from src.ui.ui import Console



if __name__ == "__main__":
    pers_repo = PersonRepo()
    pers_service =Pers_service(pers_repo)
    console = Console(pers_service)
    console.menu()
