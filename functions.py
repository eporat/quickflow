from typing import Callable, Generic, TypeVar
from stream import AlgorithmGroup, StreamAlgorithm
from statistics import mean, median

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

Max = lambda algorithms: Map(max, algorithms)
Mean = lambda algorithms: Map(mean, algorithms)
Median = lambda algorithms: Map(median, algorithms)
Min = lambda algorithms: Map(min, algorithms)