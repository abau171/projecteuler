from utils import digit

def is_palindrome(l):
    for i in range(len(l) // 2):
        if l[i] != l[-1 - i]:
            return False
    return True

def largest_palindrome_product(num_digits):
    largest = 0
    low = 10 ** (num_digits - 1)
    high = 10 * low
    print(low, high)
    for a in range(high, low, -1):
        for b in range(a, low, -1):
            product = a * b
            if product > largest and is_palindrome(digit.split(product)):
                largest = product
    return largest

print(largest_palindrome_product(3))

