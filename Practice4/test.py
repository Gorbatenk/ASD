import pytest
from class_hamster import Hamster
from practice4 import HamsterListBasic, HamsterListExtended


class TestParrotListBasic:
    def setup_method(self):
        self.hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        self.hamster2 = Hamster("Hamster2", "Breed2", "Color2", 2, 5)
        self.hamster3 = Hamster("Hamster3", "Breed3", "Color3", 3, 6)

    def test_append_and_getitem(self):
        hamster_list = HamsterListBasic()
        hamster_list.append(self.hamster1)
        hamster_list.append(self.hamster2)
        hamster_list.append(self.hamster3)
        assert hamster_list[0] == self.hamster1
        assert hamster_list[1] == self.hamster2
        assert hamster_list[2] == self.hamster3
        with pytest.raises(IndexError):
            assert hamster_list[3]

    def test_len(self):
        hamster_list = HamsterListBasic()
        hamster_list.append(self.hamster1)
        hamster_list.append(self.hamster2)
        hamster_list.append(self.hamster3)
        assert len(hamster_list) == 3

    def test_setitem(self):
        parrot_list = HamsterListBasic()
        parrot_list.append(self.hamster1)
        parrot_list.append(self.hamster2)
        parrot_list.append(self.hamster3)
        parrot_list[1] = self.hamster3
        assert parrot_list[1] == self.hamster3
        with pytest.raises(IndexError):
            parrot_list[3] = self.hamster1

    def test_index(self):
        parrot_list = HamsterListBasic()
        parrot_list.append(self.hamster1)
        parrot_list.append(self.hamster2)
        assert parrot_list.index(self.hamster2) == 1
        with pytest.raises(ValueError):
            parrot_list.index(self.hamster3)

    def test_remove(self):
        hamster_list = HamsterListBasic()
        hamster_list.append(self.hamster1)
        hamster_list.append(self.hamster2)
        hamster_list.append(self.hamster3)
        hamster_list.remove(self.hamster2)
        assert self.hamster2 not in hamster_list
        with pytest.raises(ValueError):
            hamster_list.remove(self.hamster2)


class TestParrotListExtended:
    def setup_method(self):
        self.hamster_list = HamsterListExtended()
        self.hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        self.hamster2 = Hamster("Hamster2", "Breed2", "Color2", 2, 3)
        self.hamster3 = Hamster("Hamster3", "Breed3", "Color3", 3, 2)

    def test_clear(self):
        self.hamster_list.append(self.hamster1)
        self.hamster_list.append(self.hamster2)
        self.hamster_list.clear()
        assert len(self.hamster_list) == 0
        assert self.hamster_list.head is None
        assert self.hamster_list.tail is None

    def test_extend(self):
        self.hamster_list.append(self.hamster1)
        self.hamster_list.append(self.hamster2)
        self.hamster_list.extend([self.hamster3])
        assert len(self.hamster_list) == 4
        assert self.hamster_list[1] == self.hamster1
        assert self.hamster_list[2] == self.hamster2
        assert self.hamster_list[3] == self.hamster3