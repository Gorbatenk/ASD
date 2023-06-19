import pytest
from class_hamster import Hamster
from class_structure import StructureExample


class TestStructureExample:
    def test_append(self):
        example = StructureExample()
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        hamster2 = Hamster("Hamster2", "Breed2", "Color2", 2, 5)
        example.append(hamster1)
        example.append(hamster2)
        assert example[0] == hamster1
        assert example[1] == hamster2

    def test_pop(self):
        example = StructureExample()
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        hamster2 = Hamster("Hamster2", "Breed2", "Color2", 2, 5)
        example.append(hamster1)
        example.append(hamster2)
        assert example.pop() == hamster2
        assert len(example) == 1

    def test_len(self):
        example = StructureExample()
        assert len(example) == 0
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        example.append(hamster1)
        assert len(example) == 1

    def test_contains(self):
        example = StructureExample()
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        example.append(hamster1)
        assert hamster1 in example
        hamster2 = Hamster("Hamster2", "Breed2", "Color2", 2, 5)
        assert hamster2 not in example

    def test_sort(self):
        example = StructureExample()
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        hamster2 = Hamster("Hamster2", "Breed2", "Color2", 2, 5)
        hamster3 = Hamster("Hamster3", "Breed3", "Color3", 3, 3)
        example.append(hamster3)
        example.append(hamster1)
        example.append(hamster2)
        example.sort(key=lambda h: h.age)
        assert example[0] == hamster1
        assert example[1] == hamster2
        assert example[2] == hamster3

    def test_reverse(self):
        example = StructureExample()
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        hamster2 = Hamster("Hamster2", "Breed2", "Color2", 2, 5)
        example.append(hamster1)
        example.append(hamster2)
        example.reverse()
        assert example[0] == hamster2
        assert example[1] == hamster1


if __name__ == "__main__":
    pytest.main()
