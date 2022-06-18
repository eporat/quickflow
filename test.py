from distinct_elements import FMAlgorithm
from functions import Mean
from sketch import AMSSketch
from stream import Stream, create_group
from count import ApproximateCounting
import random

a: Stream = zip([random.randint(1, 40) for _ in range(10_000)], [1] * 10_000)
fm = FMAlgorithm(epsilon=0.1)
print(len(fm))
print(fm.run(a))

b: Stream = zip([random.randint(1, 40) for _ in range(10_000)], [1] * 10_000)
algorithm1 = ApproximateCounting(epsilon=.5, delta=0.01)
algorithm2 = ApproximateCounting(epsilon=1./3, delta=0.01)
ams = Mean(create_group(AMSSketch, 100))

print(len(algorithm1))
print(len(algorithm2))
print(len(ams))

print(create_group([algorithm1, algorithm2, ams]).run(b))
