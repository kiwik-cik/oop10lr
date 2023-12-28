class Transport: # Объявление класса Transport
    def __init__(self, brand, max_speed, kind=None):  # Определение метода инициализации
        self.brand = brand  # Установка марки транспорта
        self.max_speed = max_speed  # Установка максимальной скорости
        self.kind = kind  # Установка типа транспорта
    def __str__(self):  # Определение метода для преобразования в строку
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'

class Car(Transport):  # Объявление класса Car, который наследуется от класса Transport
    def __init__(self, brand, max_speed, mileage, gasoline_residue):  # Определение метода инициализации
        super().__init__(brand, max_speed, kind='Car')  # Вызов метода инициализации родительского класса
        self.mileage = mileage  # Установка пробега
        self.__gasoline_residue = gasoline_residue  # Установка остатка бензина (приватное свойство)

    @property  # Определение декоратора для создания свойства gasoline
    def gasoline(self):  # Геттер для свойства gasoline
        return f'Осталось бензина на {self.__gasoline_residue} км'

    @gasoline.setter  # Определение сеттера для свойства gasoline
    def gasoline(self, value):  # Сеттер для свойства gasoline
        if isinstance(value, int):  # Проверка, что значение является целым числом
            self.__gasoline_residue += value  # Увеличение остатка бензина на заданное значение
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
        else:
            print('Ошибка заправки автомобиля')  # Вывод сообщения об ошибке заправки автомобиля

class Boat(Transport):  # Объявление класса Boat, который наследуется от класса Transport
    def __init__(self, brand, max_speed, owners_name):  # Определение метода инициализации
        super().__init__(brand, max_speed, kind='Boat')  # Вызов метода инициализации родительского класса
        self.owners_name = owners_name  # Установка имени владельца

    def __str__(self):  # Определение метода для преобразования в строку
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'

class Plane(Transport):  # Объявление класса Plane, который наследуется от класса Transport
    def __init__(self, brand, max_speed, capacity):  # Определение метода инициализации
        super().__init__(brand, max_speed, kind='Plane')  # Вызов метода инициализации родительского класса
        self.capacity = capacity  # Установка вместимости

    def __str__(self):  # Определение метода для преобразования в строку
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'

car = Car('Audi', 250, 10000, 50)  # Создание экземпляра класса Car
boat = Boat('Boeing', 350, 'John')  # Создание экземпляра класса Boat
plane = Plane('Boeing', 900, 300) # Создание экземпляра класса Plane

print(car) # Выводим Car
print(boat) # Выводим Boat
print(plane) # Выводим Plane
