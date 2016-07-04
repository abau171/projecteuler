from utils import cache

@cache.deterministic
def get_num_combos(coins, amount, first_usable=0):
	num_combos = 0
	for i in range(first_usable, len(coins)):
		coin = coins[i]
		if amount - coin > 0:
			num_combos += get_num_combos(coins, amount - coin, i)
		elif amount - coin == 0:
			num_combos += 1
	return num_combos

if __name__ == "__main__":
    print(get_num_combos((1, 2, 5, 10, 20, 50, 100, 200), 200))

