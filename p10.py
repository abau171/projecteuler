from utils import prime

def primes_below(n):
    g = prime.gen()
    while True:
        p = next(g)
        if p >= n:
            break
        yield p

def sum_primes_below(n):
    return sum(primes_below(n))

print(sum_primes_below(2000000))

