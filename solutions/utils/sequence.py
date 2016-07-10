import itertools

def fib(a=0, b=1):
    while True:
        yield a
        a, b = b, a + b

def triangle():
    sum_c = 0
    for c in itertools.count(1):
        sum_c += c
        yield sum_c

def adjacent(l, num_adjacent):
    for i in range(len(l) - (num_adjacent - 1)):
        yield tuple(l[i:i + num_adjacent])

