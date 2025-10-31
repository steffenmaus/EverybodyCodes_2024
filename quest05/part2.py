import re
from collections import defaultdict

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in lines]

grid = intlines
cols = []
for x in range(len(grid[0])):
    cols.append([])
for y in range(len(grid)):
    for x in range(len(grid[0])):
        cols[x].append(grid[y][x])

shouts_count = defaultdict(int)
round = 0
ans = None
while not ans:
    clapper_col = round % len(cols)
    clapper_val = cols[clapper_col].pop(0)
    clap_col = (clapper_col + 1) % len(cols)

    size = len(cols[clap_col])
    target = (clapper_val - 1) % (2 * size)
    if target > size:
        target = 2 * size - target
    cols[clap_col].insert(target, clapper_val)

    shout = "".join(str(c[0]) for c in cols)
    shouts_count[shout] += 1
    if shouts_count[shout] == 2024:
        ans = int(shout) * (round + 1)
    round += 1

print(ans)
