from utils import factor

def smallest_multiple(upper_bound):
    prime_factors = {}
    for i in range(upper_bound):
        new_factors = factor.prime_factorize(i)
        prime_factors = factor.prime_factors_union(prime_factors, new_factors)

    product = 1
    for f in prime_factors:
        product *= (f ** prime_factors[f])

    return product

print(smallest_multiple(20))

