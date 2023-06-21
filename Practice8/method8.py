from abc import ABC, abstractmethod
from class_hamster import Hamster

class AbstractStack(ABC):

    @abstractmethod
    def push(self, value: Hamster) -> None:
        pass

    @abstractmethod
    def pop(self) -> Hamster:
        pass

    @abstractmethod
    def top(self) -> Hamster:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass


class PriorityQueue(ABC):

    @abstractmethod
    def enqueue(self, value: Hamster) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Hamster:
        pass

    @abstractmethod
    def top(self) -> Hamster:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass