from typing import Callable, Generic, TypeVar, List
from stream import AlgorithmGroup, StreamAlgorithm
from statistics import mean, median
from copy import deepcopy

T = TypeVar('T')

class Map(StreamAlgorithm, Generic[T]):
    def __init__(self, func: Callable, algorithms: AlgorithmGroup, **params) -> None:
        self.func = func
        self.params = params
        self.algorithms = algorithms

    def update(self, element) -> None:
        self.algorithms.update(element)

    def __call__(self, *args) -> T:
        return self.func(self.algorithms(*args), **self.params)

    def __len__(self):
        return len(self.algorithms)

class Mean(Map[float]):
    def __init__(self, algorithms: AlgorithmGroup) -> None:
        Map.__init__(self, mean, algorithms)

class Median(Map[float]):
    def __init__(self, algorithms: AlgorithmGroup) -> None:
        Map.__init__(self, median, algorithms)