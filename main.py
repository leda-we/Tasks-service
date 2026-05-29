from models import Tasks

try:
    task1 = Tasks("Сделать чё-то", priority=5)
    print("Создано", task1)
    print("ID задачи:", task1.id)
    task1.change("In progress")
    print("После обновления:", task1)

    task1.change("ахахахахаха")
except ValueError as e:
    print(f"Ошибка валидации: {e}")
