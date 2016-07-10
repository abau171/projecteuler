def num_distinct_powers(upper_bound):
    distinct_powers = set()
    for base in range(2, upper_bound + 1):
        for power in range(2, upper_bound + 1):
            distinct_powers.add(base ** power)
    return len(distinct_powers)

if __name__ == "__main__":
    print(num_distinct_powers(100))

