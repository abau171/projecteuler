def split_fraction(d):
	next_n = 1
	n = None
	n_map = dict()
	looping = False
	while not looping:
		n = next_n
		next_n = (10 * n) % d
		if next_n == 0:
			n_map[n] = None
			break
		if n in n_map:
			looping = True
		n_map[n] = next_n
	loop_start = n if looping else None
	n = 1
	head = []
	loop = []
	while n != loop_start:
		head.append((10 * n) // d)
		n = n_map[n]
	if looping:
		loop.append((10 * n) // d)
		n = n_map[n]
		while n != loop_start:
			loop.append((10 * n) // d)
			n = n_map[n]
	return head, loop

def denom_with_largest_cycle(upper_bound):
    largest_cycle_length = -1
    cycle_d = None
    for d in range(2, upper_bound):
        head, loop = split_fraction(d)
        cycle_length = len(loop)
        if cycle_length > largest_cycle_length:
            largest_cycle_length = cycle_length
            cycle_d = d
    return cycle_d

if __name__ == "__main__":
    print(denom_with_largest_cycle(1000))

