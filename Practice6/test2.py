import time
from class_generator import Generator

generator = Generator()
hamsters = generator.generate_1000()


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def __len__(self):
        return len(self._stack)


def test_stack_performance():
    stack = Stack()
    start_time = time.time()
    for hamster in hamsters:
        stack.push(hamster)
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert len(stack) == 1000
    assert elapsed_time < 1


def test_priorqueue_performance():
    prior_queue = []
    start_time = time.time()
    for hamster in hamsters:
        prior_queue.append(hamster)
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert len(prior_queue) == 1000
    assert elapsed_time < 1
