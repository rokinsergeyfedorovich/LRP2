class Chocolate:
    """
    Базовый класс для шоколада.

    Атрибуты:
        name (str): Название шоколада
        cocoa (int): Процент какао
    """

    def __init__(self, name: str, cocoa: int) -> None:
        """
        Инициализация шоколада.

        Args:
            name: Название шоколада
            cocoa: Процент содержания какао
        """
        self.name = name
        self.cocoa = cocoa
        self._expired: bool = False  # Непубличный атрибут - статус свежести

    def __str__(self) -> str:
        """Пользовательское строковое представление."""
        return f"{self.name} ({self.cocoa}% какао)"

    def __repr__(self) -> str:
        """Официальное строковое представление."""
        return f"{self.__class__.__name__}(name='{self.name}', cocoa={self.cocoa})"

    def check_freshness(self) -> str:
        """
        Проверка свежести шоколада.
        Базовый метод.
        """
        if self._expired:
            return f"{self.name} просрочен!"
        return f"{self.name} свежий"

    def eat(self) -> str:
        """
        Употребление шоколада.
        Будет перегружаться в дочерних классах.
        """
        if self._expired:
            return "Нельзя есть просроченный шоколад!"
        return f"Вы съели {self.name}"


class MilkChocolate(Chocolate):
    """
    Класс молочного шоколада.

    Атрибуты:
        name (str): Название (наследуется)
        cocoa (int): Процент какао (наследуется)
        milk_percent (int): Процент молока
    """

    def __init__(self, name: str, cocoa: int, milk_percent: int) -> None:
        """
        Расширение конструктора.

        Args:
            name: Название шоколада
            cocoa: Процент какао
            milk_percent: Процент молока
        """
        super().__init__(name, cocoa)  # Наследование конструктора
        self.milk_percent = milk_percent

    def __str__(self) -> str:
        """Перегрузка строкового представления."""
        return f"{super().__str__()} | Молочный | Молоко: {self.milk_percent}%"

    def __repr__(self) -> str:
        """Перегрузка официального представления."""
        return f"MilkChocolate(name='{self.name}', cocoa={self.cocoa}, milk_percent={self.milk_percent})"

    def eat(self) -> str:
        """
        Перегрузка метода eat.

        Причина перегрузки: молочный шоколад нежный и тает во рту.
        """
        if self._expired:
            return "Нельзя есть просроченный молочный шоколад!"
        return f"{self.name} нежно тает во рту!"


class DarkChocolate(Chocolate):
    """
    Класс темного шоколада.

    Атрибуты:
        name (str): Название (наследуется)
        cocoa (int): Процент какао (наследуется)
        is_bitter (bool): Горький или нет
    """

    def __init__(self, name: str, cocoa: int, is_bitter: bool = True) -> None:
        """
        Расширение конструктора.

        Args:
            name: Название шоколада
            cocoa: Процент какао
            is_bitter: Горький ли шоколад
        """
        super().__init__(name, cocoa)  # Наследование конструктора
        self.is_bitter = is_bitter

    def __str__(self) -> str:
        """Перегрузка строкового представления."""
        bitter_text = "горький" if self.is_bitter else "мягкий"
        return f"{super().__str__()} | Темный | {bitter_text}"

    def __repr__(self) -> str:
        """Перегрузка официального представления."""
        return f"DarkChocolate(name='{self.name}', cocoa={self.cocoa}, is_bitter={self.is_bitter})"

    def check_freshness(self) -> str:
        """
        Перегрузка метода проверки свежести.

        Причина перегрузки: темный шоколад хранится дольше.
        """
        if self._expired:
            return f"{self.name} просрочен, но темный шоколад еще можно есть"
        return f"{self.name} свежий, можно есть"


if __name__ == "__main__":
    # Создаем объекты с уникальными именами переменных
    milk_chocolate = MilkChocolate("Аленка", 32, 25)
    dark_chocolate = DarkChocolate("Бабаевский", 75, True)

    # Тестируем методы
    print(milk_chocolate)  # Аленка (32% какао) | Молочный | Молоко: 25%
    print(dark_chocolate)  # Бабаевский (75% какао) | Темный | горький

    print(repr(milk_chocolate))  # MilkChocolate(name='Аленка', cocoa=32, milk_percent=25)
    print(repr(dark_chocolate))  # DarkChocolate(name='Бабаевский', cocoa=75, is_bitter=True)

    # Наследованный метод
    print(milk_chocolate.check_freshness())  # Аленка свежий

    # Перегруженные методы
    print(milk_chocolate.eat())  # Аленка нежно тает во рту!
    print(dark_chocolate.eat())  # Вы съели Бабаевский (унаследовано без изменений)

    # Перегруженный метод в DarkChocolate
    print(dark_chocolate.check_freshness())  # Бабаевский свежий, можно есть
