import random
from class_hamster import Hamster

class Generator:
    def generate_single(self):
        names = ["Білка", "Хрумка", "Рижик", "Шустрік", "Мишка", "Карамелька", "Тофік", "Їжачок", "Пухко", "Джері"]
        breeds = ["Золотий хом'як", "Сирійський хом'як", "Російський хом'як", "Джунгарський хом'як", "Китайський хом'я"]
        areals = ["Північна та Південна Америка", "Європа та Азія", "Африка", "Австралія"]
        colors = ["білий", "чорний", "сірий", "каштановий", "бурий", "золотистий", "рожевий", "кремовий"]
        ages = [1, 2, 3, 4, 5]

        name = random.choice(names)
        breed = random.choice(breeds)
        color = random.choice(colors)
        age = random.choice(ages)
        areal = random.choice(areals)

        return Hamster(name, breed, color, age, areal)

    def generate_1000(self):
        hamsters = [...]
        return hamsters