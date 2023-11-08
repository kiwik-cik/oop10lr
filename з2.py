class Literature:
    def __init__(self, source_code, literature_type, name, publishing_year, publishing_house, number_of_pages, author):
        self.source_code = source_code
        self.literature_type = literature_type
        self.name = name
        self.publishing_year = publishing_year
        self.publishing_house = publishing_house
        self.number_of_pages = number_of_pages
        self.author = author

    def __str__(self):
        return f"Type: {self.literature_type}\nName: {self.name}\nYear of Publishing: {self.publishing_year}\nPublisher: {self.publishing_house}\nPages: {self.number_of_pages}\nAuthor: {self.author}"


class ScientificAndTechnicalLiterature(Literature):
    def __init__(self, source_code, name, publishing_year, publishing_house, number_of_pages, author, scientific_field, number_of_copies):
        super().__init__(source_code, "scientific and technical literature", name, publishing_year, publishing_house, number_of_pages, author)
        self.scientific_field = scientific_field
        self.number_of_copies = number_of_copies

    def __str__(self):
        return super().__str__() + f"\nScientific Field: {self.scientific_field}\nNumber of Copies: {self.number_of_copies}"


class Periodicals(Literature):
    def __init__(self, source_code, name, publishing_year, publishing_house, number_of_pages, author, periodical_type, publishing_period):
        super().__init__(source_code, "periodicals", name, publishing_year, publishing_house, number_of_pages, author)
        self.periodical_type = periodical_type
        self.publishing_period = publishing_period

    def __str__(self):
        return super().__str__() + f"\nPeriodical Type: {self.periodical_type}\nPublishing Period: {self.publishing_period}"


class ReferenceBooks(Literature):
    def __init__(self, source_code, name, publishing_year, publishing_house, number_of_pages, author, field, volume, part):
        super().__init__(source_code, "reference books", name, publishing_year, publishing_house, number_of_pages, author)
        self.field = field
        self.volume = volume
        self.part = part

    def __str__(self):
        return super().__str__() + f"\nField: {self.field}\nVolume: {self.volume}\nPart: {self.part}"
scientific_book = ScientificAndTechnicalLiterature("SC123", "Physics for Scientists and Engineers", 2015, "Publisher A", 500, "John Smith", "Physics", 1000)
print(scientific_book)

periodical = Periodicals("P123", "National Geographic", 2022, "Publisher B", 80, "Various", "Magazine", "Monthly")
print(periodical)

reference = ReferenceBooks("R123", "Encyclopedia of Science", 2010, "Publisher C", 1000, "Various Authors", "Science", 5, 2)
print(reference)