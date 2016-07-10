from utils import factor

def d(n):
    divisors = factor.factorize(n)
    divisors.remove(n)
    return sum(divisors)

def sum_amicables(upper_bound):
    amicables = set()
    for a in range(2, upper_bound):
        b = d(a)
        if a != b and a == d(b):
            amicables.add(a)
    return sum(amicables)

if __name__ == "__main__":
    print(sum_amicables(10000))

