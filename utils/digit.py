def gen(n):
    if n == 0:
        yield 0
    else:
        while n > 0:
            digit = n % 10
            n = n // 10
            yield digit

def split(n):
    return list(gen(n))

