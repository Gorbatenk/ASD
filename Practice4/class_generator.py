import random
from class_hamster import Hamster


class Generator:
    @staticmethod
    def generate_hamster() -> Hamster:
        names = ["Білка", "Хрумка", "Рижик", "Шустрік", "Мишка", "Карамелька", "Тофік", "Їжачок", "Пухко", "Джері"]
        breeds = ["Золотий хом'як", "Сирійський хом'як", "Російський хом'як", "Джунгарський хом'як", "Китайський хом'я"]
        areals = ["Північна та Південна Америка", "Європа та Азія", "Африка", "Австралія"]
        colors = ["білий", "чорний", "сірий", "каштановий", "бурий", "золотистий", "рожевий", "кремовий"]

        # Згенерувати випадкові значення для кожного атрибута хом'яка
        name = random.choice(names)
        breed = random.choice(breeds)
        areal = random.choice(areals)
        age = random.randint(1, 3)
        color = random.choice(colors)

        # Створити об'єкт хом'яка з випадковими атрибутами
        hamster = Hamster(name, breed, areal, age, color)
        return hamster


    def generate_1000(self) -> list:

      plist = list()
      for i in range(1000):
        plist.append(self.generate_hamster())
      return plist


    def generate_10_000(self) -> list:
      plist = [self.generate_hamster() for _ in range(10000)]
      return plist

    def generate_single(self) -> list:
        plist = [self.generate_hamster()]
        return plist


# Створити випадкову хом`яка
random_hamster = Generator().generate_hamster()

# Вивід повідомлення про випадкового хом`яка
message = random_hamster.generate_message()
print(message)


def abstract_object():
    return None
