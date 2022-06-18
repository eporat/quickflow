from functions import Mean, Median
from stream import StreamAlgorithm, create_group
import random
from math import ceil, log2
from numpy import uint8

class MorrisAlgorithm(StreamAlgorithm[int]):
    def __init__(self) -> None:
        self.X: uint8 = 0

    def update(self, _) -> None:
        if random.random() <= 1.0 / 2**self.X:
            self.X += 1

    def __call__(self) -> int:
        return int(2**self.X - 1)

MorrisPlus = lambda epsilon: Mean(create_group(MorrisAlgorithm, count=ceil(1.5/epsilon ** 2)))
MorrisPlusPlus = lambda epsilon, delta: Median(create_group(MorrisPlus, count=max(1, ceil(log2(1/delta))), epsilon=epsilon))
ApproximateCounting = MorrisPlusPlus