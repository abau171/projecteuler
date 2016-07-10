from utils import factor

def largest_prime_factor(n):
    return max(factor.gen_prime(n))

print(largest_prime_factor(600851475143))

