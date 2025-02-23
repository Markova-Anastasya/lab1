class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int):
        """
        Конструктор класса Animal.
        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self._name = name  # Инкапсуляция имени, так как изменение должно происходить через методы
        self.age = age

    def __str__(self) -> str:
        return f"Животное: {self._name}, возраст: {self.age} лет"

    def __repr__(self) -> str:
        return f"Animal(name={self._name!r}, age={self.age})"

    def make_sound(self) -> str:
        """
        Метод, который должны переопределить дочерние классы.
        """
        return "Неизвестный звук"

    def get_name(self) -> str:
        """
        Геттер для получения имени животного.
        """
        return self._name


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор класса Dog.
        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self.breed = breed

    def __str__(self) -> str:
        return f"Собака: {self._name}, порода: {self.breed}, возраст: {self.age} лет"

    def __repr__(self) -> str:
        return f"Dog(name={self._name!r}, age={self.age}, breed={self.breed!r})"

    def make_sound(self) -> str:
        """
        Переопределенный метод из базового класса.
        Собака лает, поэтому изменяем поведение метода.
        """
        return "Гав-гав"


class Cat(Animal):
    """
    Дочерний класс, представляющий кошку.
    """

    def __init__(self, name: str, age: int, color: str):
        """
        Конструктор класса Cat.
        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)
        self.color = color

    def __str__(self) -> str:
        return f"Кошка: {self._name}, цвет: {self.color}, возраст: {self.age} лет"

    def __repr__(self) -> str:
        return f"Cat(name={self._name!r}, age={self.age}, color={self.color!r})"

    def make_sound(self) -> str:
        """
        Переопределенный метод из базового класса.
        Кошка мяукает, поэтому изменяем поведение метода.
        """
        return "Мяу-мяу"


if __name__ == "__main__":
    dog = Dog("Барон", 3, "Немецкая овчарка")
    cat = Cat("Мурка", 2, "Рыжий")

    print(dog)  
    print(cat)

    print(dog.make_sound())
    print(cat.make_sound())