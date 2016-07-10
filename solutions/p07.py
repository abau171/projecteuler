from utils import prime

def nth_prime(n):
    g = prime.gen()
    for i in range(n - 1):
        next(g)
    return next(g)

print(nth_prime(10001))

