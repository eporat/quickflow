from functions import Map, Mean
from math_utils import MAX_128_INT, md5, random128
from stream import Element, StreamAlgorithm, create_group
from math import ceil

class FMAlgorithmHelper(StreamAlgorithm[float]):
    def __init__(self) -> None:
        self.z = 1
        self.random = random128()

    def update(self, element: Element):
        self.z = min(self.z, md5(element[0] ^ self.random) / MAX_128_INT)

    def __call__(self) -> float:
        return self.z

FMAlgorithm = lambda epsilon: Map(lambda z: 1.0/z - 1, 
    Mean(
        create_group(FMAlgorithmHelper, count=ceil(1./epsilon**2))
    ))