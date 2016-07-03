from utils import prime

def smallest_prime(n):
    for p in prime.gen():
        if n % p == 0:
            return p

def gen_prime(n):
    while n > 1:
        p = smallest_prime(n)
        yield p
        n //= p

def prime_factorize(n):
    prime_factors = dict()
    for p in gen_prime(n):
        if p in prime_factors:
            prime_factors[p] += 1
        else:
            prime_factors[p] = 1
    return prime_factors

def prime_factors_union(a, b):
    common_factors = set(a.keys()).union(set(b.keys()))
    union_factors = dict()
    for factor in common_factors:
        union_factors[factor] = max(a.get(factor, 0), b.get(factor, 0))
    return union_factors

def factorize(n):
    factors = set()
    factors.add(1)
    for p in gen_prime(n):
        for factor in tuple(factors):
            factors.add(p * factor)
    return factors

