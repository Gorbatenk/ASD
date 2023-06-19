class StructureExample:
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value

    def __delitem__(self, index):
        del self._list[index]

    def __iter__(self):
        return iter(self._list)

    def __contains__(self, value):
        return value in self._list

    def append(self, item):
        self._list.append(item)

    def extend(self, values):
        self._list.extend(values)

    def insert(self, index, value):
        self._list.insert(index, value)

    def remove(self, value):
        self._list.remove(value)

    def pop(self, index=-1):
        return self._list.pop(index)

    def clear(self):
        self._list.clear()

    def sort(self, key=None, reverse=False):
        self._list.sort(key=key, reverse=reverse)

    def reverse(self):
        self._list.reverse()

    def __str__(self):
        return str(self._list)
