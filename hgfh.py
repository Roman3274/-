from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    def get_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"



class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"


class Cat(Animal):
    def make_sound(self):
        return "Няв-няв!"


class Parrot(Animal):
    def make_sound(self):
        return "Привіт!"


animals = [
    Dog("Барсик", 3),
    Cat("Мурка", 2),
    Parrot("Кеша", 4)
]

for animal in animals:
    print(animal.get_info())
    print("Каже:", animal.make_sound())
    print("-" * 20)

