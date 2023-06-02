class Hamster:
    def __repr__(self) -> str:
        return f"Hamster(name={self.name}, breed={self.breed}, areal={self.areal}, age={self.age}, color={self.color})"

    def __init__(self, name: str, breed: str, areal: str, age: int, color: str):
        self.name = name
        self.breed = breed
        self.areal = areal
        self.age = age
        self.color = color

    def determine_age_category(self) -> str:
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
        age_category = self.determine_age_category()
        areal_category = self.determine_areal_category()
        message = f"Хом'як {self.name} має забарвлення {self.color}, {age_category} вік {self.age}  " \
                  f"і відноситься до породи {self.breed}, які Живуть у {areal_category} регіоні."
        return message


# Запрос данных у пользователя
name = input("Введіть ім'я хом'яка: ")
breed = input("Введіть породу хом'яка: ")
areal = input("Введіть регіон хом'яка (Північна та Південна Америка, Європа та Азія, Африка, Австралія): ")
age = int(input("Введіть вік хом'яка: "))
color = input("Введіть забарвлення хом'яка: ")

# Створення об'єкту класу Hamster
hamster = Hamster(name, breed, areal, age, color)

# Вивід повідомлення про хом'яка
message = hamster.generate_message()
print(message)

# Вихідні дані не коректні
hamster1 = Hamster("Сашко", "Золотий хом'як", "Північна Америка", "3 роки", "золотистий")

# Порода невідома
hamster2 = Hamster("Папу", "невідома порода", "Австралія", 2, "коричневий")
