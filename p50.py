from utils import prime

def consecutive_prime_sum_len(p, min_len):
    upper = prime.gen()
    lower = prime.gen()
    cur_sum = 0
    n = 0
    while True:
        if cur_sum < p:
            cur_sum += next(upper)
            n += 1
        elif cur_sum > p:
            if n < min_len:
                return 0
            cur_sum -= next(lower)
            n -= 1
        else:
            return n

def longest_consecutive_prime_sum(upper_bound):
    longest = 0
    max_sum_len = 0
    for p in prime.gen():
        if p >= upper_bound:
            break
        sum_len = consecutive_prime_sum_len(p, max_sum_len)
        if sum_len > max_sum_len:
            longest = p
            max_sum_len = sum_len
    return longest

if __name__ == "__main__":
    print(longest_consecutive_prime_sum(1000000))

