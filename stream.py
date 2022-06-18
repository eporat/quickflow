from abc import ABC, abstractmethod
from typing import Callable, Iterable, Union, Tuple, Any, Generic, TypeVar

Element = Tuple[int, float]
T = TypeVar('T')
Stream = Iterable[Element]


class StreamAlgorithm(ABC, Generic[T]):
    @abstractmethod
    def update(self, element) -> None:
        pass

    @abstractmethod
    def __call__(self, *args) -> Any:
        pass

    def run(self, stream: Stream) -> Any:
        for element in stream:
            self.update(element)
        
        return self()

    def __len__(self) -> int:
        if hasattr(self, 'algorithm'):
            return len(self.algorithm)

        return 1

class AlgorithmGroup(StreamAlgorithm):
    def __init__(self, algorithms):
        self.algorithms = algorithms

    def update(self, element):
        for algorithm in self.algorithms:
            algorithm.update(element)
    
    def __call__(self, *args):
        return [algorithm(*args) for algorithm in self.algorithms]
    
    def __len__(self) -> int:
        return sum(len(algorithm) for algorithm in self.algorithms)

def create_group(x: Any, count: int = None, *args, **kwargs):
    if isinstance(x, list):
        return AlgorithmGroup(x)
    
    if not isinstance(x, Callable):
        raise TypeError("create_group takes as input a list of stream algorithms or a callable")
    if count < 1:
        raise ValueError("count cannot be less than 1 in create_group")

    return AlgorithmGroup([x(*args, **kwargs) for _ in range(count)])