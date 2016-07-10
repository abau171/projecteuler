from utils import factor

def is_abundant(n):
    divisors = factor.factorize(n)
    divisors.remove(n)
    return sum(divisors) > n

def is_sum(n, nums):
    for m in nums:
        if n - m in nums:
            return True
    return False

def non_abundant_sums():
    abundants = set(n for n in range(12, 28123) if is_abundant(n))
    return sum(n for n in range(28123) if not is_sum(n, abundants))

if __name__ == "__main__":
    print(non_abundant_sums())

