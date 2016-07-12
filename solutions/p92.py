from utils import cache
from utils import digit

def sum_digit_squares(n):
    return sum(d * d for d in digit.split(n))

def chain_end(n):
    if n == 1 or n == 89:
        return n
    else:
        return cached_chain_end(sum_digit_squares(n))

cached_chain_end = cache.deterministic(chain_end)

def count_89s(upper_bound):
    count = 0
    for i in range(1, upper_bound):
        if chain_end(i) == 89:
            count += 1
    return count

if __name__ == "__main__":
    print(count_89s(10000000))

