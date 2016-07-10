def num_int_right_tris(p):
    n = 0
    for a in range(1, p):
        for b in range(a, p):
            c = p - a - b
            if c <= 0:
                break
            if a * a + b * b == c * c:
                n += 1
    return n

def max_int_right_tris(max_perim):
    max_n = -1
    p_max_n = None
    for p in range(max_perim + 1):
        n = num_int_right_tris(p)
        if n > max_n:
            max_n = n
            p_max_n = p
    return p_max_n

if __name__ == "__main__":
    print(max_int_right_tris(1000))

