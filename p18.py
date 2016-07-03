from utils import cache
from utils import sequence

def max_route_sum(triangle_list):
    paths = None
    for row in reversed(triangle_list):
        if paths is None:
            paths = [0] * len(row)
        else:
            paths = [max(*pair) for pair in sequence.adjacent(paths, 2)]
        for i in range(len(row)):
            paths[i] += row[i]
    return paths[0]

input_str = """\
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23\
"""

def parse_triangle_list(triangle_str):
    triangle_list = []
    for row_str in triangle_str.split("\n"):
        triangle_list.append([int(num_str) for num_str in row_str.split(" ")])
    return triangle_list

if __name__ == "__main__":
    print(max_route_sum(parse_triangle_list(input_str)))

