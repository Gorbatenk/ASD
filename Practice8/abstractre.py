from abc import ABC, abstractmethod
from typing import Iterable, Optional
from class_hamster import Hamster


class AbstractObject:
    pass


class HamsterObject(AbstractObject):
    def __init__(self, hamster):
        self.hamster = hamster

    def __eq__(self, other):
        if isinstance(other, HamsterObject):
            return self.hamster == other.hamster
        return False

    def __lt__(self, other):
        if isinstance(other, HamsterObject):
            return self.hamster < other.hamster
        return NotImplemented

    def __str__(self):
        return str(self.hamster)


class AbstractTree(ABC):
    @abstractmethod
    def insert(self, obj: AbstractObject):
        pass

    @abstractmethod
    def remove(self, obj: AbstractObject):
        pass

    @abstractmethod
    def find(self, obj: AbstractObject) -> Optional[AbstractObject]:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def __iter__(self) -> Iterable[AbstractObject]:
        pass


class AbstractTreeExtended(AbstractTree):
    def is_properly_implemented(self) -> bool:
        return True


class AbstractTreeBasic(AbstractTree):
    def __init__(self):
        self.objects = []

    def insert(self, obj: AbstractObject):
        self.objects.append(obj)

    def remove(self, obj: AbstractObject):
        if obj in self.objects:
            self.objects.remove(obj)

    def find(self, obj: AbstractObject) -> Optional[AbstractObject]:
        if obj in self.objects:
            return obj
        return None

    def is_empty(self) -> bool:
        return len(self.objects) == 0

    def size(self) -> int:
        return len(self.objects)

    def __iter__(self) -> Iterable[AbstractObject]:
        return iter(self.objects)


class AbstractBinaryTree(AbstractTreeExtended, AbstractTreeBasic):
    def insert(self, obj: AbstractObject):
        # Placeholder implementation
        pass

    def remove(self, obj: AbstractObject):
        # Placeholder implementation
        pass

    def find(self, obj: AbstractObject) -> Optional[AbstractObject]:
        # Placeholder implementation
        pass


# Example usage:

# Creating a Hamster instance
hamster = Hamster("Fluffy", "Syrian", "Golden", 2, "Європа та Азія")

# Creating a HamsterObject instance
hamster_obj = HamsterObject(hamster)

# Creating an AbstractBinaryTree instance
tree = AbstractBinaryTree()

# Inserting the HamsterObject into the tree
tree.insert(hamster_obj)

# Retrieving the HamsterObject from the tree
retrieved_obj = tree.find(hamster_obj)

# Removing the HamsterObject from the tree
tree.remove(hamster_obj)

# Checking if the tree is empty
is_empty = tree.is_empty()

# Getting the size of the tree
tree_size = tree.size()

# Iterating over the objects in the tree
for obj in tree:
    print(obj)

# Checking if the tree is properly implemented
is_properly_implemented = tree.is_properly_implemented()
