from class_hamster import Hamster
from class_structure import StructureExample
from class_generator import Generator


class Find(StructureExample):
    def find(self, value):
        for i, item in enumerate(self._list):
            if item == value:
                return i
        return None

    def append(self, item):
        self._list.append(item)

    def find(self, value):
        for i, item in enumerate(self._list):
            if item == value:
                return i
        return None

    def find_by(self, value: Hamster):
        for (i, item) in enumerate(self._list):
            if item == value:
                return i
        return None

    def find_by_attr(self, value: Hamster, attr: str):
        if isinstance(value, list):
            for (i, item) in enumerate(self._list):
                if all(getattr(item, attr, None) == getattr(v, attr, None) for v in value):
                    return i
        else:
            for (i, item) in enumerate(self._list):
                if getattr(item, attr, None) == getattr(value, attr, None):
                    return i
        return None

    @staticmethod
    def exponential_search(self: list[Hamster], value: Hamster) -> int | None:
        if self[0] == value:
            return 0

        i = 1
        n = len(self)
        while i < n and self[i] <= value:
            i *= 2

        left = i // 2
        right = min(i, n - 1)

        while left <= right:
            mid = (left + right) // 2
            if self[mid] == value:
                return mid
            elif self[mid] < value:
                left = mid + 1
            else:
                right = mid - 1

        return None

    def find_index(self, value: Hamster) -> int | None:
        return self.exponential_search(self._list, value)

    @staticmethod
    def binary_search(self: list[Hamster], value: Hamster) -> int | None:
        left = 0
        right = len(self) - 1

        while left <= right:
            mid = (left + right) // 2
            if self[mid] == value:
                return mid
            elif self[mid] < value:
                left = mid + 1
            else:
                right = mid - 1

        return None

    def find_binary(self, value: Hamster) -> int | None:
        return self.binary_search(self._list, value)


if __name__ == "__main__":
    gen = Generator()
    pl = [gen.generate_single() for _ in range(5)]
    for s in pl:
        print(s)

    f = Find()
    f.append(pl[0])
    f.append(pl[1])
    f.append(pl[2])
    f.append(pl[3])
    f.append(pl[4])

    print(f)
    print(f.find(pl[0]))

