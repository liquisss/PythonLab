import json
import xml.etree.ElementTree as ET
import xml.dom.minidom


# Класс для обработки собственного исключения
class InvalidYearError(Exception):
    pass


# абстрактный класс
class Movie:
    def __init__(self, title, year, director, genre):
        self.title = title
        # Обработка собственного исключения
        if not isinstance(year, int):
            raise InvalidYearError("Year must be an integer.")
        self.year = year
        self.director = director
        self.genre = genre

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "director": self.director,
            "genre": self.genre
        }


# наследуемый класс
class Films(Movie):
    def __init__(self, title, year, director, genre, actor, description):
        super().__init__(title, year, director, genre)
        self.actor = actor
        self.description = description

    def to_dict(self):
        films_dict = super().to_dict()
        films_dict.update(
            {
                "actor": self.actor,
                "description": self.description
            }
        )
        return films_dict


# наследуемый класс
class Serial(Movie):
    def __init__(self, title, year, director, genre, actor, description, seasons):
        super().__init__(title, year, director, genre)
        self.actor = actor
        self.description = description
        self.seasons = seasons

    def to_dict(self):
        serials_dict = super().to_dict()
        serials_dict.update(
            {
                "actor": self.actor,
                "description": self.description,
                "seasons": self.seasons
            }
        )
        return serials_dict


# создание объектов классов
film_1 = Films("We", 2019, "Jordan Peele",
               "horror", "Evan Alex", "very scary")
film_2 = Films("Red Notice", 2021, "Rawson Marshall Thurber",
               "Comedy", "Gal Gadot", "very interesting(maybe)")
serial_1 = Serial("Queen's move", 2022, "Scott Frank",
                  "Historical drama", "Anya Taylor-Joy",
                  "very smart woman", 1)
serial_2 = Serial("Man vs Bee", 2022, "Rowan Atkinson",
                  "comedy", "Jingo Lucy",
                  "strange incomprehensible", 1)

# словарь из объектов классов
dict_movie = {
    "films": [film_1.to_dict(), film_2.to_dict()],
    "serials": [serial_1.to_dict(), serial_2.to_dict()]
}

# запись в файл out.json
with open('out.json', 'w') as json_file:
    json.dump(dict_movie, json_file, indent=4)

# обработка ошибки открытия файла
try:
    # чтение из файла input.json
    with open('input.json', 'r', encoding='utf-8') as input_file:
        for line in input_file:
            print(line)
except FileNotFoundError:
    print("File not found")

# запись в XML-файл
# создаем XML-структуру
root = xml.dom.minidom.Document()  # Создание нового XML-документа
root_element = root.createElement("media")  # Создание корневого элемента "media"
root.appendChild(root_element)  # Добавление корневого элемента в документ

# Цикл для обработки каждого объекта
for film in [film_1, film_2]:
    movie_element = root.createElement("film")  # Создание элемента "film"
    root_element.appendChild(movie_element)  # Добавление элемента "film" в корневой элемент
    for key, value in film.to_dict().items():
        element = root.createElement(key)  # Создание элемента с ключом
        element.appendChild(root.createTextNode(str(value)))  # Добавление текстового узла со значением в элемент
        movie_element.appendChild(element)  # Добавление элемента в элемент "film"

for serial in [serial_1, serial_2]:
    serial_element = root.createElement("serial")
    root_element.appendChild(serial_element)
    for key, value in serial.to_dict().items():
        element = root.createElement(key)
        element.appendChild(root.createTextNode(str(value)))
        serial_element.appendChild(element)

xml_str = root.toprettyxml(indent="  ")  # Форматирование XML-документа с отступами

with open("out.xml", "w") as file:  # Открытие файла "media.xml" для записи
    file.write(xml_str)

# Считывание данных из XML-файла
tree = ET.parse("out.xml")
root = tree.getroot()

# Обход элементов "film"
for film_element in root.iter("film"):
    # Извлечение данных из элементов
    film_data = {}
    for child_element in film_element:
        film_data[child_element.tag] = child_element.text
    print("Movie:", film_data)

# Обход элементов "serial"
for serial_element in root.iter("serial"):
    # Извлечение данных из элементов
    serial_data = {}
    for child_element in serial_element:
        serial_data[child_element.tag] = child_element.text
    print("TV Show:", serial_data)
