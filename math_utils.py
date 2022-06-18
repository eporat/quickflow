import random
import hashlib

# TODO: Choose better prime
PRIME = 18446744073709551557
MAX_128_INT = 2**128 - 1

def hash(x):
    return int(hashlib.md5(str(x).encode('ASCII')).hexdigest(), 16)

def random128():
    return random.randint(0, MAX_128_INT)
    
class KWiseIndependentGenerator:
    """
    K-Wise Independent random number generator works only for 64-bit numbers
    """
    def __init__(self, k: int, randbits: int = 64) -> None:
        self.rs = [random.getrandbits(randbits) for _ in range(k)]
        self.k = k

    def __call__(self, i: int):
        # Horner's method: https://en.wikipedia.org/wiki/Horner%27s_method
        b = self.rs[0]

        for j in range(1, self.k):
            b = (self.rs[j] + (b*i) % PRIME) % PRIME

        return b