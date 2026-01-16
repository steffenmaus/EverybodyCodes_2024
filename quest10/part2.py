with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]


def calc_power(word):
    out = 0
    for i, c in enumerate(word, 1):
        out += i * (ord(c) - 64)
    return out


def find_match(p, maze):
    x, y = p
    candidates = set([maze[(x2, y)] for x2 in range(8)]) & set([maze[(x, y2)] for y2 in range(8)]) - {"."}
    return candidates.pop()


def get_runic_word(x_offset, y_offset):
    maze = {}
    for y in range(8):
        for x in range(8):
            maze[(x, y)] = lines[y_offset + y][x_offset + x]

    out = ""
    for y in range(2, 6):
        for x in range(2, 6):
            out += find_match((x, y), maze)

    return out


total = 0
for y in range(0, len(lines), 9):
    for x in range(0, len(lines[0]), 9):
        total += calc_power(get_runic_word(x, y))

print(total)
