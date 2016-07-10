zero_to_nineteen_str = [
	"zero",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
	"ten",
	"eleven",
	"twelve",
	"thirteen",
	"fourteen",
	"fifteen",
	"sixteen",
	"seventeen",
	"eighteen",
	"nineteen"
]

tens_str = [
	"twenty",
	"thirty",
	"forty",
	"fifty",
	"sixty",
	"seventy",
	"eighty",
	"ninety"
]

def num_to_word(n):
	if n < 20:
		return zero_to_nineteen_str[n]
	elif n < 100:
		tens = n // 10
		part = n % 10
		result = tens_str[tens - 2]
		if part != 0:
			result += num_to_word(part)
		return result
	elif n < 1000:
		hundreds = n // 100
		part = n % 100
		result = num_to_word(hundreds) + "hundred"
		if part != 0:
			result += "and" + num_to_word(part)
		return result
	elif n < 1000000:
		thousands = n // 1000
		part = n % 1000
		result = num_to_word(thousands) + "thousand"
		if part != 0:
			result += num_to_word(part)
		return result

def letter_count(upper_bound):
    return sum(
        len(num_to_word(n))
        for n in range(1, upper_bound + 1))

if __name__ == "__main__":
    print(letter_count(1000))

