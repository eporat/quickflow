from stream import Element, StreamAlgorithm
import random

class ReservoirSampling(StreamAlgorithm[int]):
    def __init__(self) -> None:
        self.s = None
        self.j = 0

    def update(self, element: Element):
        for _ in range(element[1]):
            if random.random() < 1.0 / self.j:
                self.s = element[0]
            self.j += 1

    def __call__(self) -> int:
        return self.s