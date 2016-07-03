from utils import prime

def gen_composites():
    n = 9
    while True:
        if not prime.contains(n):
            yield n
        n += 2

def gen_squares():
    n = 1
    while True:
        yield n * n
        n += 1

def other_conjecture(n):
    for s in gen_squares():
        if 2 * s > n:
            return False
        elif prime.contains(n - 2 * s):
            return True

def smallest_failure():
    for c in gen_composites():
        if not other_conjecture(c):
            return c

if __name__ == "__main__":
    print(smallest_failure())

