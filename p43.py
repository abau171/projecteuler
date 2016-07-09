from utils import prime
from utils import digit

prime_gen = prime.gen()
primes = [next(prime_gen) for _ in range(7)]

def num_substring_divs(last=[], remaining=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    if len(last) == 10:
        return digit.join(last)
    n = 0
    for ri in range(len(remaining)):
        cur = last + [remaining[ri]]
        if len(cur) >= 4:
            sub = digit.join(cur[len(cur) - 3:len(cur)])
            p = primes[len(cur) - 4]
            if sub % p == 0:
                n += num_substring_divs(
                    cur,
                    remaining[:ri] + remaining[ri + 1:])
        else:
            n += num_substring_divs(
                cur,
                remaining[:ri] + remaining[ri + 1:])
    return n

if __name__ == "__main__":
    print(num_substring_divs())

