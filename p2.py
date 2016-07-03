from utils import fib

def sum_even_fib(upper_bound):
    even_sum = 0
    g = fib.gen(2, 3)
    n = next(g)
    while n <= upper_bound:
        even_sum += n
        next(g)
        next(g)
        n = next(g)
    return even_sum

print(sum_even_fib(4000000))

