from utils import cache

_known_primes = set()
_greatest_known_prime = None

@cache.deterministic_gen
def gen():
    # builds a dynamically-growing Sieve of Eratosthenes
    sieve = dict()
    candidate = 2
    while True:
        if candidate not in sieve:
            # candidate is prime (not divisible by primes less than itself)
            _known_primes.add(candidate)
            _greatest_known_prime = candidate
            yield candidate
            # lesser primes handle all cases until candidate * candidate, so start there
            sieve[candidate * candidate] = [candidate]
        else:
            # candidate is not prime
            # for prime factors of candidate in sieve, eliminate their next lowest multiple
            for prime in sieve[candidate]:
                sieve.setdefault(candidate + prime, []).append(prime)
            # we're past this point now, free up unused memory
            del sieve[candidate]
        candidate += 1

_contains_gen = gen()

def contains(n):
    # if it is a known prime, return immediately
    if n in _known_primes:
        return True
    # if it is less than the greatest known prime, and not a known prime, it is not a prime
    elif _greatest_known_prime is not None:
        if n < _greatest_known_prime:
            return False
    # search unknown primes until the number is found, or is skipped over
    for prime in _contains_gen:
        if prime == n:
            return True
        elif prime > n:
            return False

