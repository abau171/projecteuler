from utils import cache

def prod(i):
    product = 1
    for factor in i:
        product *= factor
    return product

@cache.deterministic
def fact(i):
    if i <= 1:
        return 1
    else:
        return i * fact(i - 1)

