import itertools

from utils import sequence

def first_n_digit_fib(n):
    target = 10 ** (n - 1)
    g = sequence.fib(1, 1)
    for i in itertools.count(1):
        if next(g) >= target:
            return i

if __name__ == "__main__":
    print(first_n_digit_fib(1000))

