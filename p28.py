def gen_spiral_diagonals(spiral_dim):
    largest_num = spiral_dim * spiral_dim
    n = 1
    step = 2
    while n < largest_num:
        for i in range(4):
            yield n
            n += step
        step += 2
    yield n

def sum_spiral_diagonals(spiral_dim):
    return sum(gen_spiral_diagonals(spiral_dim))

if __name__ == "__main__":
    print(sum_spiral_diagonals(1001))

