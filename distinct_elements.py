import hashlib
import random
from functions import Mean
from math_utils import MAX_128_INT, random128
from stream import Element, StreamAlgorithm, create_group
from statistics import mean

class FMAlgorithmHelper(StreamAlgorithm[float]):
    def __init__(self) -> None:
        self.z = 1
        self.random = random128()

    def update(self, element: Element):
        self.z = min(self.z, hash(element[0] ^ self.random) / MAX_128_INT)

    def __call__(self) -> float:
        return self.z

class FMAlgorithm(StreamAlgorithm[float]):
    def __init__(self, epsilon) -> None:
        self.epsilon = epsilon
        self.algorithm = Mean(create_group(FMAlgorithmHelper, count=int(1./epsilon**2)))

    def update(self, element: Element):
        self.algorithm.update(element)

    def __call__(self) -> float:
        return 1. / self.algorithm() - 1