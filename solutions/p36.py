from utils import digit

def gen_sides(num_digits):
    start = int(10 ** (num_digits - 1))
    end = int(10 ** num_digits)
    for left_num in range(start, end):
        left = digit.split(left_num)
        right = list(reversed(left))
        yield left, right

def gen_pals():
    for i in range(10):
        yield i
    i = 0
    while True:
        i += 1
        for left, right in gen_sides(i):
            yield digit.join(left + right)
        for left, right in gen_sides(i):
            for j in range(10):
                yield digit.join(left + [j] + right)

def get_bin_digits(n):
    bin_digits = []
    while n > 0:
        bin_digits.insert(0, n % 2)
        n //= 2
    return bin_digits

def is_pal(l):
    for i in range(len(l) // 2):
        if l[i] != l[-i - 1]:
            return False
    return True

def get_sum_double_pals(upper_bound):
    double_pal_sum = 0
    for pal in gen_pals():
        if pal >= upper_bound:
            break
        if is_pal(get_bin_digits(pal)):
            double_pal_sum += pal
    return double_pal_sum

if __name__ == "__main__":
    print(get_sum_double_pals(1000000))

