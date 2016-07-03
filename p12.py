from utils import sequence
from utils import factor

def highly_divisible_triangle(num_divisors):
    for n in sequence.triangle():
        num_factors = len(factor.factorize(n))
        if num_factors > num_divisors:
            return n

print(highly_divisible_triangle(500))

