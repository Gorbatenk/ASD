class StructureExample:
    _list = []

    def __len__(self):
        return len(self._list)

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value

    def __delitem__(self, index):
        del self._list[index]

    def append(self, item):
        self._list.append(item)

    def remove(self, item):
        self._list.remove(item)

    def __iter__(self):
        return iter(self._list)
