from utils import prime
from utils import digit

def is_pandigital(n):
    digits = digit.split(n)
    digits.sort()
    for i in range(0, len(digits)):
        if digits[i] != i + 1:
            return False
    return True

def largest_pandigital():
    for n in reversed(range(10000000)): # all 8- and 9-digit pandigitals are divisible by 3
        if is_pandigital(n) and prime.contains(n):
            return n

if __name__ == "__main__":
    print(largest_pandigital())

