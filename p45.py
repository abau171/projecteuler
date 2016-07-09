import itertools

def t(n):
    return (n * (n + 1)) // 2

def p(n):
    return (n * (3 * n - 1)) // 2

def h(n):
    return n * (2 * n - 1)

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
h_contains = contains_func(h)

def next_tph(last_tn):
    for tn in itertools.count(last_tn + 1):
        tri = t(tn)
        if p_contains(tri) and h_contains(tri):
            return tri

if __name__ == "__main__":
    print(next_tph(285))

