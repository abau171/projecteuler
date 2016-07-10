def sum_squares(n):
    return sum(i * i for i in range(1, n + 1))

def square_sum(n):
    n_sum = sum(range(1, n + 1))
    return n_sum * n_sum

def sum_square_diff(n):
    return square_sum(n) - sum_squares(n)

print(sum_square_diff(100))

