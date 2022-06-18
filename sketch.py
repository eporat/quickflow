from math import ceil, log2
from functions import Mean, Median, Min
from math_utils import random_sign, md5, random128
from stream import Element, StreamAlgorithm, create_group

class AMSSketch(StreamAlgorithm[float]):
    def __init__(self) -> None:
        self.r = random_sign(k=4)
        self.Z = 0

    def update(self, element: Element):
        self.Z += self.r(element[0]) * element[1]

    def __call__(self) -> float:
        return self.Z ** 2

AMSPlus = lambda epsilon: Mean(create_group(AMSSketch, count=ceil(1./epsilon ** 2)))

class CountMin(StreamAlgorithm[float]):
    def __init__(self, epsilon) -> None:
        self.w = ceil(4/epsilon)
        self.random = random128()
        self.h = lambda x: md5(x ^ self.random) % self.w
        self.s = [0] * self.w
    
    def update(self, element: Element):
        self.s[self.h(element[0])] += element[1]

    def __call__(self, i: int) -> float:
        return self.s[self.h(i)] 

CountMinPlus = lambda epsilon, n: Min(create_group(CountMin, ceil(log2(n)), epsilon=epsilon))
CountMinPlusPlus = lambda epsilon, n: Median(create_group(CountMinPlus, ceil(log2(n)), epsilon=epsilon, n=n))

class CountSketch(StreamAlgorithm[float]):
    def __init__(self, epsilon) -> None:
        self.w = ceil(4/epsilon**2)
        self.r = random128()
        self.h = lambda x: md5(x ^ self.r) % self.w
        self.s = [0] * self.w
        self.random = random_sign(k=4)

    def update(self, element: Element):
        self.s[self.h(element[0])] += element[1] * self.random(element[0])

    def __call__(self, i: int) -> float:
        return self.s[self.h(i)] * self.random(i)