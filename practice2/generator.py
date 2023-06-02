import random
from typing import List

class Hamster:
    def __init__(self, name: str, breed: str, areal: str, age: int, color: str):
        self.name = name
        self.breed = breed
        self.areal = areal
        self.age = age
        self.color = color

    def determine_size_category(self) -> str:
        if self.age > 3:
            return "старий"
        elif self.age > 2:
            return "дорослий"
        elif self.age > 1:
            return "підліток"
        else:
            return "невеликий"

    def determine_areal_category(self) -> str:
        areal_categories = {
            "Північна та Південна Америка": "американському",
            "Європа та Азія": "євроазіатському",
            "Африка": "африканському",
            "Австралія": "австралійському"
        }
        return areal_categories.get(self.areal, "невідомому")

    def generate_message(self) -> str:
        age_category = self.determine_size_category()
        areal_category = self.determine_areal_category()
        message = f"Хом'як {self.name} має забарвлення {self.color}, {age_category} вік {self.age} " \
                  f"і належить до породи {self.breed}, які живуть у {areal_category} регіоні."
        return message


class Generator:
    @staticmethod
    def generate_parrot() -> Hamster:
        names = ["Білка", "Хрумка", "Рижик", "Шустрік", "Мишка", "Карамелька", "Тофік", "Їжачок", "Пухко", "Джері"]
        breeds = ["Золотий хом'як", "Сирійський хом'як", "Російський хом'як", "Джунгарський хом'як", "Китайський хом'як"]
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


# Створити випадкового хом'яка
random_parrot = Generator.generate_parrot()

# Створити повідомлення для випадкового хом'яка
message = random_parrot.generate_message()
print(message)


def generate_parrots(num_parrots: int) -> List[Hamster]:
    parrots = []
    for _ in range(num_parrots):
        parrot = Generator.generate_parrot()
        parrots.append(parrot)
    return parrots


# Згенерувати список з 1000 випадкових хом'яків
parrots_list_1000 = generate_parrots(1000)

# Згенерувати список з 10000 випадкових хом'яків
parrots_list_10000 = generate_parrots(10000)