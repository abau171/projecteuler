import itertools

from utils import digit

def gen_champernowne_digits():
    for n in itertools.count(1):
        for d in digit.split(n):
            yield d

def d(i):
    g = gen_champernowne_digits()
    for _ in range(i - 1):
        next(g)
    return next(g)

def d_powers_of_ten(n):
    product = 1
    for i in range(n):
        product *= d(10 ** i)
    return product

if __name__ == "__main__":
    print(d_powers_of_ten(7))

