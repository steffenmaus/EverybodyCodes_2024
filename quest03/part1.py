with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


X = len(lines[0])
Y = len(lines)

out = 0

prev = set()
for y in range(Y):
    for x in range(X):
        if lines[y][x] == "#":
            prev.add((x, y))

while prev:
    out += len(prev)
    next = set()
    for p in prev:
        if all([n in prev for n in get_all_nei_2d_4(p)]):
            next.add(p)
    prev = next
print(out)
