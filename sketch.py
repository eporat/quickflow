from math import log2
from functions import Mean
from math_utils import KWiseIndependentGenerator, hash, random128
from stream import Element, StreamAlgorithm, create_group

class AMSSketch(StreamAlgorithm[float]):
    def __init__(self) -> None:
        self.random = KWiseIndependentGenerator(4)
        self.Z = 0

    def update(self, element: Element):
        self.Z += (2 * (self.random(element[0]) % 2) - 1) * element[1]

    def __call__(self) -> float:
        return self.Z ** 2

AMSPlus = lambda epsilon: Mean(create_group(AMSSketch, count=int(1./epsilon ** 2)))

class CountMin(StreamAlgorithm[float]):
    def __init__(self, epsilon) -> None:
        self.w = int(4/epsilon)
        self.random = random128()
        self.h = lambda x: hash(x ^ self.random) % self.w
        self.s = [0] * self.w
    
    def update(self, element: Element):
        self.s[self.h(element[0])] += element[1]

    def __call__(self, i: int) -> float:
        return self.s[self.h(i)] 

class CountMinPlus(StreamAlgorithm[float]):
    def __init__(self, epsilon, n) -> None:
        self.algorithms = create_group(CountMin, int(log2(n)), epsilon=epsilon)
    
    def update(self, element: Element):
        self.algorithms.update(element)

    def __call__(self, i: int) -> float:
        return min(self.algorithms(i))