with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    r = [p for p in r if p in maze]
    return r


palms = set()
maze = set()
for x in range(len(lines[0])):
    for y in range(len(lines)):
        p = (x, y)
        c = lines[y][x]
        match c:
            case "P":
                palms.add(p)
                maze.add(p)
            case ".":
                maze.add(p)

open = {(0, 1)}
done = set()
steps = 0
while open:
    done |= open
    if all([p in done for p in palms]):
        break
    next_open = set()
    for o in open:
        for n in get_all_nei(o):
            if n not in done:
                next_open.add(n)
    open = next_open
    steps += 1

print(steps)
