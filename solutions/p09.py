from utils.general import *

def is_pythagorean_triplet(a, b, c):
    return a * a + b * b == c * c

def find_triplet_from_sum(n_sum):
    for c in range(1, n_sum + 1):
        for b in range(1, n_sum + 1):
            a = n_sum - b - c
            if is_pythagorean_triplet(a, b, c):
                return a, b, c

print(prod(find_triplet_from_sum(1000)))

