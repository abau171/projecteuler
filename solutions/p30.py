from utils import digit

def gen_digit_powers(n, power):
	for d in digit.split(n):
		yield d ** power

def gen_sum_digit_powers(power):

	max_num_digits = 1
	while max_num_digits * (9 ** power) > (10 ** max_num_digits) - 1:
		max_num_digits += 1

	max_search = 10 ** max_num_digits

	for i in range(2, max_search):
		if i == sum(gen_digit_powers(i, power)):
			yield i

def sum_sum_digit_powers(power):
    return sum(gen_sum_digit_powers(power))

if __name__ == "__main__":
    print(sum_sum_digit_powers(5))

