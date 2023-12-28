class Literature:
    # Определение конструктора класса
    def __init__(self, source_code, literature_type, name, publishing_year, publishing_house, number_of_pages, author):
        self.source_code = source_code  # Установка исходного кода
        self.literature_type = literature_type  # Установка типа литературы
        self.name = name  # Установка названия
        self.publishing_year = publishing_year  # Установка года издания
        self.publishing_house = publishing_house  # Установка издательства
        self.number_of_pages = number_of_pages  # Установка количества страниц
        self.author = author  # Установка автора

    # Определение метода для получения строкового представления объекта
    def __str__(self):
        return f"Type: {self.literature_type}\nName: {self.name}\nYear of Publishing: {self.publishing_year}\nPublisher: {self.publishing_house}\nPages: {self.number_of_pages}\nAuthor: {self.author}"


class ScientificAndTechnicalLiterature(Literature):
    # Определение конструктора подкласса
    def __init__(self, source_code, name, publishing_year, publishing_house, number_of_pages, author, scientific_field, number_of_copies):
        super().__init__(source_code, "scientific and technical literature", name, publishing_year, publishing_house, number_of_pages, author)
        self.scientific_field = scientific_field  # Установка научной области
        self.number_of_copies = number_of_copies  # Установка количества копий

    # Определение метода для получения строкового представления объекта
    def __str__(self):
        return super().__str__() + f"\nScientific Field: {self.scientific_field}\nNumber of Copies: {self.number_of_copies}"


class Periodicals(Literature):
    # Определение конструктора подкласса
    def __init__(self, source_code, name, publishing_year, publishing_house, number_of_pages, author, periodical_type, publishing_period):
        super().__init__(source_code, "periodicals", name, publishing_year, publishing_house, number_of_pages, author)
        self.periodical_type = periodical_type  # Установка типа периодики
        self.publishing_period = publishing_period  # Установка периодичности издания

    # Определение метода для получения строкового представления объекта
    def __str__(self):
        return super().__str__() + f"\nPeriodical Type: {self.periodical_type}\nPublishing Period: {self.publishing_period}"

class ReferenceBooks(Literature):
    def __init__(self, source_code, name, publishing_year, publishing_house, number_of_pages, author, field, volume, part):
        # Вызов конструктора родительского класса Literature
        super().__init__(source_code, "reference books", name, publishing_year, 
                         publishing_house, number_of_pages, author)
        self.field = field  # Установка области
        self.volume = volume  # Установка объема
        self.part = part  # Установка части

    # Определение метода для получения строкового представления объекта
    def __str__(self):
        return super().__str__() + f"\nField: {self.field}\nVolume: {self.volume}\nPart: {self.part}"

# Создание экземпляра класса ScientificAndTechnicalLiterature
scientific_book = ScientificAndTechnicalLiterature("SC123", "Physics for Scientists and Engineers", 
                                                  2015, "Publisher A", 500, "John Smith", "Physics", 1000)
print(scientific_book)  # Вывод информации о книге

# Создание экземпляра класса Periodicals
periodical = Periodicals("P123", "National Geographic", 2022, "Publisher B", 80, "Various", "Magazine", "Monthly")
print(periodical)  # Вывод информации о периодике

# Создание экземпляра класса ReferenceBooks
reference = ReferenceBooks("R123", "Encyclopedia of Science", 2010, "Publisher C", 1000, "Various Authors", "Science", 5, 2)
print(reference)  # Вывод информации о справочнике
