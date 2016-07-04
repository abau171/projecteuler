from utils import prime
from utils import digit

def is_left_truncatable(digits):
    while len(digits) > 1:
        digits = digits[1:]
        if not prime.contains(digit.join(digits)):
            return False
    return True

def is_right_truncatable(digits):
    while len(digits) > 1:
        digits = digits[:-1]
        if not prime.contains(digit.join(digits)):
            return False
    return True

def is_truncatable(p):
    digits = digit.split(p)
    return is_left_truncatable(digits) and is_right_truncatable(digits)

def gen_truncatable_primes():

    g = prime.gen()
    # get rid of 2, 3, 5, and 7
    for _ in range(4):
        next(g)

    for p in g:
        if is_truncatable(p):
            yield p

def sum_truncatable_primes():
    tp_sum = 0
    g = gen_truncatable_primes()
    for _ in range(11):
        tp_sum += next(g)
    return tp_sum

if __name__ == "__main__":
    print(sum_truncatable_primes())

