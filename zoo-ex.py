# 1. Родительский класс
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return f"{name} издает звук"


# 2. Пресмыкающееся
class Reptile(Animal):
    def show(self):
        return f"Пресмыкающееся {self.name}: ползет по канату!"


# 3. Земноводное
class Amphibian(Animal):
    def show(self):
        return f"Земноводное {self.name}: прыгает в воду!"


# 4. Класс шоу
class ZooShow:
    def __init__(self, animals):
        self.animals = animals

    def start(self):
        print("=== ЗООШОУ ===")
        price = input("Выберите билет (1 - Обычный 500, 2 - VIP 1000): ")

        print("\nПрограмма выступления:")
        for a in self.animals:
            print(a.show())


# Запуск
animals_list = [Reptile("Питон", 3), Amphibian("Лягушка", 1)]
show = ZooShow(animals_list)
show.start()