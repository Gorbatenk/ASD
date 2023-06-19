class Hamster:
    """All methods which needs personally to hamster"""
    name: str  # hamster name
    breed: str  # hamster breed
    age: int  # hamster age
    color: str  # hamster genderclass Hamster:

    def __init__(self, name, breed, color, age, areal):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.areal = areal

    def __eq__(self, other):
        if isinstance(other, Hamster):
            return (
                self.name == other.name
                and self.breed == other.breed
                and self.color == other.color
                and self.age == other.age
                and self.areal == other.areal
            )
        return False

    def __lt__(self, other):
        if isinstance(other, Hamster):
            return self.age < other.age
        return NotImplemented

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

    def __str__(self):
        return self.generate_message()

