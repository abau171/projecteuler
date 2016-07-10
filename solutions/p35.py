from utils import prime
from utils import digit

def rotate_digits(digits):
    digits.append(digits.pop(0))

def is_circular_prime(p):
    digits = digit.split(p)
    for _ in range(len(digits) - 1):
        rotate_digits(digits)
        if not prime.contains(digit.join(digits)):
            return False
    return True

def num_circular_primes(upper_bound):
    n = 0
    for p in prime.gen():
        if p > upper_bound:
            break
        if is_circular_prime(p):
            n += 1
    return n

if __name__ == "__main__":
    print(num_circular_primes(1000000))

