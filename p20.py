from utils.general import *
from utils import digit

def fact_digit_sum(n):
    return sum(digit.split(fact(n)))

if __name__ == "__main__":
    print(fact_digit_sum(100))

