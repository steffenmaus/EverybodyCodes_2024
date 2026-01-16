with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

maze = {}
for y in range(8):
    for x in range(8):
        maze[(x, y)] = lines[y][x]


def find_match(p):
    x, y = p
    candidates = set([maze[(x2, y)] for x2 in range(8)]) & set([maze[(x, y2)] for y2 in range(8)]) - {"."}
    return candidates.pop()


out = ""
for y in range(2, 6):
    for x in range(2, 6):
        out += find_match((x, y))

print(out)
