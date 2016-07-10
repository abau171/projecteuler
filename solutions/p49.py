from utils import prime
from utils import digit

def n_digit_primes(n):
    for p in prime.gen():
        if p >= 10 ** (n + 1):
            break
        elif p < 10 ** n:
            yield p

def digit_combos(num_digits):
    dc = dict()
    for p in n_digit_primes(4):
        comb = tuple(sorted(digit.split(p)))
        dc.setdefault(comb, []).append(p)
    return dc

def filter_combo_len(dc, min_len):
    filtered = dict()
    for key in dc:
        if len(dc[key]) >= min_len:
            filtered[key] = dc[key]
    return filtered

def arithmetic_triples(l):
    for ai in range(len(l) - 2):
        for bi in range(ai + 1, len(l) - 1):
            c = 2 * l[bi] - l[ai]
            for ci in range(bi + 1, len(l)):
                if l[ci] == c:
                    yield l[ai], l[bi], l[ci]

def prime_perms():
    combos = filter_combo_len(digit_combos(4), 3)
    for l in combos.values():
        yield from arithmetic_triples(l)

if __name__ == "__main__":
    for a, b, c in prime_perms():
        concat = a * 100000000 + b * 10000 + c
        if concat != 148748178147:
            print(concat)

