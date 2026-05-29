import uuid
from datetime import datetime

class Sup:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()

class Tasks(Sup):
    def __init__(self, title: str, priority: int = 1):
        super().__init__()
        self.title = title
        self.__status = "New"
        self.priority = priority
    @property
    def status(self) -> str:
        return self.__status
    
    def change(self, new_status: str):
        allow_status = ["New", "In progress", "Complete", "Archive"]
        if new_status in allow_status:
            self.__status = new_status
        else:
            raise ValueError(f"Статус {new_status} не поддерживается системой.")
    
    def __repr__(self):
        return f"<Task [{self.status}] {self.title} (Priority: {self.priority})>"
    