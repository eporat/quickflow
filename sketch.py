from pseudorandom import KWiseIndependentGenerator
from stream import Element, StreamAlgorithm
import random

class AMSSketch(StreamAlgorithm[float]):
    def __init__(self) -> None:
        self.random = KWiseIndependentGenerator(4)
        self.Z = 0

    def update(self, element: Element):
        self.Z += (2 * (self.random(element[0]) % 2) - 1) * element[1]

    def __call__(self) -> float:
        return self.Z ** 2