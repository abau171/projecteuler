import itertools

from utils import factor

def first_n(n):
    run = 0
    for i in itertools.count(2):
        num_distinct_primes = len(factor.prime_factorize(i).keys())
        if num_distinct_primes == n:
            run += 1
        else:
            run = 0
        if run == n:
            return i + 1 - n

if __name__ == "__main__":
    print(first_n(4))

