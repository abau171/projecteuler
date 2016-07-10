import itertools

def nth_perm(l, n):
    for i, p in enumerate(itertools.permutations(l)):
        if i == n - 1:
            return p

if __name__ == "__main__":
    print(nth_perm((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 1000000))

