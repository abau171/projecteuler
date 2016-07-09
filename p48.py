def sum_self_powers(upper_bound):
    return sum(i ** i for i in range(1, upper_bound + 1))

if __name__ == "__main__":
    print(str(sum_self_powers(1000))[-10:])

