import itertools

from utils import digit

def is_pandigital(digits):
    has_digit = [False] * 10
    for d in digits:
        if d == 0:
            return False
        if has_digit[d]:
            return False
        has_digit[d] = True
    return True

def gen_pandigital_multiples():
    for i in range(2, 100000):
        digits = []
        for n in itertools.count(1):
            digits += digit.split(i * n)
            if len(digits) > 9:
                break
            if len(digits) == 9 and is_pandigital(digits):
                yield digit.join(digits)

if __name__ == "__main__":
    print(max(gen_pandigital_multiples()))

