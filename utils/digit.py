def gen(n):
    if n == 0:
        yield 0
    else:
        while n > 0:
            digit = n % 10
            n = n // 10
            yield digit

def split(n):
    digits = list(gen(n))
    digits.reverse()
    return digits

def join(digits):
    n = 0
    for d in digits:
        n *= 10
        n += d
    return n

