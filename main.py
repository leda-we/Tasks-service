from models import Tasks, User

try:
    task1 = Tasks("Сделать чё-то", priority=5)
    print("Создано", task1)
    print("ID задачи:", task1.id)
    task1.change("In progress")
    print("После обновления:", task1)
    user = User("admin", "developer")
    print( user.username, user.role)

    task1.change("ахахахахаха")
except ValueError as e:
    print(f"Ошибка валидации: {e}")
