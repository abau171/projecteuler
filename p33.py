import fractions

from utils.general import *
from utils import digit

def is_digit_cancelling(numer, denom):
    n_digits = digit.split(numer)
    d_digits = digit.split(denom)
    f = fractions.Fraction(numer, denom)
    for i in range(len(n_digits)):
        cancelled = n_digits[i]
        n_remaining = digit.join(n_digits[:i] + n_digits[i + 1:])
        for j in range(len(d_digits)):
            if d_digits[j] == cancelled:
                d_remaining = digit.join(d_digits[:j] + d_digits[j + 1:])
                if f == fractions.Fraction(n_remaining, d_remaining):
                    return True
    return False

def gen_cancelling_fractions():
    for denom in range(11, 100):
        if denom % 10 == 0:
            continue
        for numer in range(10, denom):
            if is_digit_cancelling(numer, denom):
                yield fractions.Fraction(numer, denom)

def denom_prod_cancelling_fractions():
    return prod(gen_cancelling_fractions()).denominator

if __name__ == "__main__":
    print(denom_prod_cancelling_fractions())

