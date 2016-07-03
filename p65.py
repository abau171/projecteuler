import itertools
import fractions

from utils import digit

def e_sequence():
    for n in itertools.count(1):
        yield 1
        yield 2 * n
        yield 1

def build_frac(seq, depth):
    if depth == 1:
        return 0
    a = next(seq)
    f = build_frac(seq, depth - 1)
    return fractions.Fraction(1, a + f)

def nth_e_convergent(n):
    return 2 + build_frac(e_sequence(), n)

def nth_e_convergent_num_sum(n):
    c = nth_e_convergent(n)
    return sum(digit.split(c.numerator))

if __name__ == "__main__":
    print(nth_e_convergent_num_sum(100))

