import pytest
from class_hamster import Hamster
from abstractlimitstructure_p5 import Stack, PriorQueue


class TestStack:
    def test_push_pop(self):
        stack = Stack()
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        hamster2 = Hamster("Hamster2", "Breed2", "Color2", 2, 5)
        hamster3 = Hamster("Hamster3", "Breed3", "Color3", 3, 3)
        stack.push(hamster1)
        stack.push(hamster2)
        stack.push(hamster3)
        assert stack.pop() == hamster3
        assert stack.pop() == hamster2
        assert stack.pop() == hamster1

    def test_pop_empty_stack(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.pop()

    def test_top(self):
        stack = Stack()
        with pytest.raises(IndexError):
            stack.top()
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        stack.push(hamster1)
        assert stack.top() == hamster1

    def test_len(self):
        stack = Stack()
        assert len(stack) == 0
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        stack.push(hamster1)
        assert len(stack) == 1

    def test_repr(self):
        stack = Stack()
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        hamster2 = Hamster("Hamster2", "Breed2", "Color2", 2, 5)
        stack.push(hamster1)
        stack.push(hamster2)
        expected_repr = repr(stack)
        assert repr(stack) == expected_repr


class TestPriorQueue:
    def test_enqueue_dequeue(self):
        queue = PriorQueue()
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        hamster2 = Hamster("Hamster2", "Breed2", "Color2", 2, 5)
        hamster3 = Hamster("Hamster3", "Breed3", "Color3", 3, 3)
        queue.enqueue(hamster1)
        queue.enqueue(hamster2)
        queue.enqueue(hamster3)
        assert queue.dequeue().age == 3

    def test_dequeue_empty_queue(self):
        queue = PriorQueue()
        with pytest.raises(IndexError):
            queue.dequeue()

    def test_is_empty(self):
        queue = PriorQueue()
        assert queue.is_empty()
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        queue.enqueue(hamster1)
        assert not queue.is_empty()

    def test_size(self):
        queue = PriorQueue()
        assert queue.size() == 0
        hamster1 = Hamster("Hamster1", "Breed1", "Color1", 1, 4)
        queue.enqueue(hamster1)
        assert queue.size() == 1
