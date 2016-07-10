from utils import cache

@cache.deterministic
def collatz_length(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz_length(n // 2)
    else:
        return 1 + collatz_length(3 * n + 1)

def longest_collatz(upper_bound):
    longest = 0
    longest_start = 0
    for i in range(1, upper_bound):
        cl = collatz_length(i)
        if cl > longest:
            longest = cl
            longest_start = i
    return longest_start

print(longest_collatz(1000000))

