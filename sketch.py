from stream import Element, StreamAlgorithm
import random

class AMSSketch(StreamAlgorithm[float]):
    def __init__(self, size) -> None:
        self.rs = [2 * random.randint(0, 1) - 1 for _ in range(size)]
        self.Z = 0

    def update(self, element: Element):
        self.Z += self.rs[element[0]] * element[1]

    def __call__(self) -> float:
        return self.Z ** 2