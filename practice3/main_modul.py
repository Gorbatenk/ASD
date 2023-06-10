class Hamster:
    """All methods which needs personally to hamster"""
    name: str  # hamster name
    breed: str  # hamster breed
    age: int  # hamster age
    color: str  # hamster genderclass Hamster:
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
