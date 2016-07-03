def count_multiples(bases, upper_bound):
    multiples = set()
    for base in bases:
        for i in range(base, upper_bound, base):
            multiples.add(i)
    return sum(multiples)

print(count_multiples([3, 5], 1000))

