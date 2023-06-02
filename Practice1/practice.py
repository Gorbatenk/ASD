class Hamster:
    def __init__(self, name, breed, areal, age, color):
        self.name = name
        self.breed = breed
        self.areal = areal
        self.age = int(age)
        self.color = color

    def determine_age(self):
        if self.age > 3:
            return "старий"
        elif self.age > 2:
            return "дорослий"
        elif self.age > 1:
            return "підліток"
        else:
            return "невеликий"

    def determine_areal(self):
        if self.areal == "Північна та Південна Америка":
            return "американському"
        elif self.areal == "Європа та Азія":
            return "євроазіатському"
        elif self.areal == "Африка":
            return "африканському"
        elif self.areal == "Австралія":
            return "австралійському"
        else:
            return "невідомому"

    def generate_message(self):
        age_category = self.determine_age()
        areal_category = self.determine_areal()
        message = f"Хом'як {self.name} має забарвлення {self.color}, {age_category} вік {self.age}  " \
                  f"і відноситься до породи {self.breed}, які Живуть у {areal_category} регіоні."
        return message


# Запрос данных у пользователя
name = input("Введіть ім'я хом'яка: ")
breed = input("Введіть породу хом'яка: ")
areal = input("Введіть регіон хом'яка (Північна та Південна Америка, Європа та Азія, Африка, Австралія): ")
age = input("Введіть вік хом'яка ")
color = input("Введіть забарвлення хом'яка: ")

# Створення об'єкту класу Hamster
hamster = Hamster(name, breed, areal, age, color)

# Вивід повідомлення про хом'яка
message = hamster.generate_message()
print(message)
