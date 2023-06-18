from abstractlimitstructure_p5 import Stack, PriorQueue
import time
from class_generator import Generator

generator = Generator()
hamsters = generator.generate_1000()

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
    prior_queue = PriorQueue()
    start_time = time.time()
    for hamster in hamsters:
        prior_queue.enqueue(hamster)
    end_time = time.time()
    elapsed_time = end_time - start_time
    assert prior_queue.size() == 1000
    assert elapsed_time < 1
