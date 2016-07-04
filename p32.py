import math

def is_pandigital(s):
    if len(s) != 9:
        return False
    found_digits = [False] * 10
    for digit_str in s:
        digit = int(digit_str)
        if digit == 0:
            return False
        elif found_digits[digit]:
            return False
        else:
            found_digits[digit] = True
    return True

def gen_pandigital_products():
    a = 1
    while True:
        num_digits_a = 1 + int(math.log10(a))
        num_digits_b = 10 - 2 * num_digits_a
        if num_digits_b <= 0:
            break
        if num_digits_b * 2 + num_digits_a > 10:
            num_digits_b = (10 - num_digits_a) // 2
        for b in range(a, 10 ** num_digits_b):
            if is_pandigital("{}{}{}".format(a, b, a * b)):
                yield a * b
        a += 1

def sum_distinct_pandigital_products():
    return sum(set(gen_pandigital_products()))

if __name__ == "__main__":
    print(sum_distinct_pandigital_products())

