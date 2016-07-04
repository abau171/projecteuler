from utils import prime

def quad_prime_coeffs(bound):
    longest_a = None
    longest_b = None
    longest_run = 0
    for a in range(1 - bound, bound):
        for b in prime.gen():
            if b >= bound:
                break
            n = 1 # when n == 0, b is already known to be prime
            #stops where n produces the first non-prime, which is also the run length
            while prime.contains((n * n) + (a * n) + b):
                n += 1
            if n > longest_run:
                longest_a = a
                longest_b = b
                longest_run = n
    return longest_a, longest_b

if __name__ == "__main__":
    a, b = quad_prime_coeffs(1000)
    print(a * b)

