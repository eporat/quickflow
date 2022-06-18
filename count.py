from functions import Mean, Median
from stream import StreamAlgorithm, create_group
import random
from math import log2

class MorrisAlgorithm(StreamAlgorithm[int]):
    def __init__(self) -> None:
        super().__init__()
        self.X = 0

    def update(self, _) -> None:
        if random.random() <= 1.0 / 2**self.X:
            self.X += 1

    def __call__(self) -> int:
        return int(2**self.X - 1)

class MorrisPlus(Mean):
    def __init__(self, epsilon):
        Mean.__init__(self, create_group(MorrisAlgorithm, count=int(1.5/epsilon ** 2)))

class MorrisPlusPlus(Median):
    def __init__(self, epsilon, delta):
        count = max(1, int(log2(1/delta)))
        Median.__init__(self, create_group(MorrisPlus, count=count, epsilon=epsilon))

ApproximateCounting = MorrisPlusPlus