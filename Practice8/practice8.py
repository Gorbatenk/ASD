from __future__ import annotations
from typing import Iterable
from class_hamster import Hamster
from abstractre import AbstractTreeBasic


class TreeNode:
    value: Hamster
    left_hamster: None | TreeNode
    right_hamster: None | TreeNode

    def __init__(self, value, left_hamster: TreeNode | None = None, right_hamster: TreeNode | None = None):
        self.value = value
        self.left_hamster = left_hamster
        self.right_hamster = right_hamster

    def __repr__(self) -> str:
        return f"TreeNode(value:{self.value}, " \
               f"left:{self.left_hamster is not None}," \
               f" right:{self.left_hamster is not None})"


class HamsterTreeBasic(AbstractTreeBasic):
    def __init__(self, *args: Iterable[Hamster]):
        self.root = None
        for hamster in args:
            self.insert(hamster)

    def __len__(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left_hamster) + self._count_nodes(node.right_hamster)

    def __repr__(self) -> str:
        return self._tree_repr(self.root)

    def _tree_repr(self, node: TreeNode) -> str:
        if node is None:
            return "None"
        return f"TreeNode({node.value}, {self._tree_repr(node.left_hamster)}, {self._tree_repr(node.right_hamster)})"

    def insert(self, value: Hamster) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: TreeNode, value: Hamster) -> TreeNode:
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left_hamster = self._insert(node.left_hamster, value)
        else:
            node.right_hamster = self._insert(node.right_hamster, value)
        return node

    def find(self, value: Hamster) -> bool:
        return self._find(self.root, value)

    def _find(self, node: TreeNode, value: Hamster) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._find(node.left_hamster, value)
        return self._find(node.right_hamster, value)

    def remove(self, value: Hamster) -> None:
        self.root = self._remove(self.root, value)

    def _remove(self, node: TreeNode, value: Hamster) -> TreeNode:
        if node is None:
            return None
        if value < node.value:
            node.left_hamster = self._remove(node.left_hamster, value)
        elif value > node.value:
            node.right_hamster = self._remove(node.right_hamster, value)
        else:
            if node.left_hamster is None:
                return node.right_hamster
            if node.right_hamster is None:
                return node.left_hamster
            min_right = self._min(node.right_hamster)
            node.value = min_right
            node.right_hamster = self._remove(node.right_hamster, min_right)
        return node

    def min(self) -> Hamster:
        return self._min(self.root)

    def _min(self, node: TreeNode) -> Hamster:
        if node.left_hamster is None:
            return node.value
        return self._min(node.left_hamster)


class HamsterTreeExtended(HamsterTreeBasic):
    def __init__(self):
        super().__init__()
        self._iter_current = None

    def clear(self) -> None:
        self.root = None

    def replace(self, oldvalue: Hamster, newvalue: Hamster) -> None:
        self.remove(oldvalue)
        self.insert(newvalue)

    def __iter__(self) -> Iterable:
        self._iter_current = None
        return self

    def __next__(self) -> Hamster:
        if self._iter_current is None:
            self._iter_current = self.min()
        else:
            self._iter_current = self._next(self.root, self._iter_current)
            if self._iter_current is None:
                raise StopIteration
        return self._iter_current

    def _next(self, node: TreeNode, value: Hamster) -> Hamster:
        if node is None:
            return None

        if value < node.value:
            left_next = self._next(node.left_hamster, value)
            return left_next if left_next is not None else node.value

        return self._next(node.right_hamster, value)

    def extend(self, values: Iterable[Hamster]) -> None:
        for value in values:
            self.insert(value)

    def count(self, value: Hamster) -> int:
        return 1 if self.find(value) else 0


class HamsterTreeBonus(HamsterTreeExtended):
    def max(self) -> Hamster:
        if self.root is None:
            return None
        return self._find_max(self.root).value

    @staticmethod
    def _find_max(node: TreeNode) -> TreeNode:
        while node.right_hamster is not None:
            node = node.right_hamster
        return node

    def __add__(self, other) -> HamsterTreeBonus:
        if not isinstance(other, HamsterTreeBonus):
            raise TypeError("Can only add instances of HamsterTreeBonus")
        new_tree = HamsterTreeBonus()
        new_tree.extend(self.traversal())
        new_tree.extend(other.traversal())
        return new_tree

    def __mul__(self, other) -> HamsterTreeBonus:
        if not isinstance(other, HamsterTreeBonus):
            raise TypeError("Can only multiply instances of HamsterTreeBonus")
        new_tree = HamsterTreeBonus()
        for hamster1 in self.traversal():
            for hamster2 in other.traversal():
                if hamster1 == hamster2:
                    new_tree.insert(hamster1)
        return new_tree

    def traversal(self) -> list[Hamster]:
        return self._traversal(self.root)

    def _traversal(self, node: TreeNode) -> list[Hamster]:
        if node is None:
            return []
        return self._traversal(node.left_hamster) + [node.value] + self._traversal(node.right_hamster)
