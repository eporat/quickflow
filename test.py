from sketch import AMSSketch
from stream import Stream, gather
from count import ApproximateCounting

a: Stream = enumerate(iter([1] * 100))
algorithm1 = ApproximateCounting(epsilon=0.5, delta=0.01)
algorithm2 = ApproximateCounting(epsilon=0.1, delta=0.01)
ams = AMSSketch(100)

print(gather([algorithm1, algorithm2, ams]).run(a))