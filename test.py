from functions import Mean
from sketch import AMSSketch
from stream import Stream, create_group
from count import ApproximateCounting

a: Stream = enumerate(iter([1] * 1_000))
algorithm1 = ApproximateCounting(epsilon=0.5, delta=0.01)
algorithm2 = ApproximateCounting(epsilon=1./3, delta=0.01)
ams = Mean(create_group(AMSSketch, 100))

print(len(algorithm1))
print(len(algorithm2))
print(len(ams))

print(create_group([algorithm1, algorithm2, ams]).run(a))
