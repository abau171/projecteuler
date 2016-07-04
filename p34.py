from utils.general import *
from utils import cache
from utils import digit

@cache.deterministic
def digit_fact(digits):
    if len(digits) == 1:
        return fact(digits[0])
    else:
        center = len(digits) // 2
        return (digit_fact(digits[:center]) +
                digit_fact(digits[center:]))

def digit_facts_sum_rec(digits, last_change):
    n_value = digit.join(digits)
    n_digit_fact = digit_fact(digits)
    digit_facts_sum = 0
    if n_value == n_digit_fact:
        digit_facts_sum += n_value
    if n_value >= n_digit_fact:
        for i in range(last_change, len(digits)):
            if digits[i] < 9:
                digits[i] += 1
                digit_facts_sum += digit_facts_sum_rec(digits, i)
                digits[i] -= 1
    return digit_facts_sum

def digit_facts_sum(num_digits):
    digits = [1] + [0] * (num_digits - 1)
    return digit_facts_sum_rec(digits, 0)

def all_digit_facts_sum():
    for i in range(2, 6):
        yield digit_facts_sum(i)

if __name__ == "__main__":
    print(sum(all_digit_facts_sum()))

