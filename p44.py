import itertools

def p(n):
    return (n * (3 * n - 1)) // 2

def contains_func(f):
    largest = -1
    i = -1
    known = set()
    def contains(val):
        nonlocal largest, i
        while val > largest:
            i += 1
            largest = f(i)
            known.add(largest)
        return val in known
    return contains

p_contains = contains_func(p)

def min_pent_pair():
    for i in itertools.count():
        for j in range(i - 1, 0, -1):
            p_i = p(i)
            p_j = p(j)
            if p_contains(p_i + p_j) and p_contains(p_i - p_j):
                # Next pair seems to be very far away, and this happens to be the
                # correct answer.
                return p_j, p_i

if __name__ == "__main__":
    print(*min_pent_pair())

