from typing import Callable, Generic, TypeVar
from stream import AlgorithmGroup, StreamAlgorithm
from statistics import mean, median

T = TypeVar('T')

class Map(StreamAlgorithm, Generic[T]):
    def __init__(self, func: Callable, algorithm: AlgorithmGroup, **params) -> None:
        self.func = func
        self.params = params
        self.algorithm = algorithm

    def update(self, element) -> None:
        self.algorithm.update(element)

    def __call__(self, *args) -> T:
        return self.func(self.algorithm(*args), **self.params)
        
Max = lambda algorithms: Map(max, algorithms)
Mean = lambda algorithms: Map(mean, algorithms)
Median = lambda algorithms: Map(median, algorithms)
Min = lambda algorithms: Map(min, algorithms)