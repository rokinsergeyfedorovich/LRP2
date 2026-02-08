import doctest


class Phone:
    def __init__(self, model: str, storage: int, power: bool):
        self.model = model
        if not isinstance(storage, int):
            raise TypeError("Хранилище должно быть типа int")
        if storage <= 0:
            raise ValueError("Хранилище должно быть положительным числом")
        self.storage = storage
        if not isinstance(power, bool):
            raise TypeError("Питание должно быть типа bool")
        self.power = power

    def is_turn_on(self) -> bool:
        """
        Функция которая проверяет включен ли телефон

        :return: Включен ли телефон

        Примеры:
        phone = Phone(xiaomi ,256, True)
        phone.is_turn_on()
        """
        ...

    def turn_on_phone(self) -> None:
        """
        Включить телефон

        :return: Телефон включен

        :raise ValueError: Если телефон был включен до этого

        Примеры:
        phone = Phone(xiaomi ,256, True)
        phone.turn_on_phone()
        """
        ...

    def turn_off_phone(self) -> None:
        """
        Выключить телефон

        :return: Телефон выключен

        :raise ValueError: Если телефон был выключен до этого

        Примеры:
        phone = Phone(xiaomi ,256, True)
        phone.turn_off_phone()
        """
        ...


class Painting:
    def __init__(self, author: str, colors: str):
        self.author = author
        self.colors = colors

    def hang_painting(self) -> None:
        """
        Повесить картину

        :return: Картина повешена
        """
        ...

    def remove_painting(self) -> None:
        """
        Снять картину

        :return: Картина снята
        """
        ...


class Pants:
    def __init__(self, brand, belt: bool, material):
        self.brand = brand
        if not isinstance(belt, bool):
            raise TypeError("Ремень должно быть типа bool")
        self.belt = belt
        self.material = material

    def check_pocket(self) -> bool:
        """
        Функция проверяет есть ли что-нибудь в карманах

        :return: Наполнен ли карман
        """
        ...

    def wear_belt(self) -> None:
        """
        Надеть ремень

        :return: Ремень надет

        :raise ValueError: Если ремень уже был надет до этого
        """
        ...

    def remove_belt(self) -> None:
        """
        Снять ремень

        :return: Ремень снят

        :raise ValueError: Если ремня не было на штанах
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
