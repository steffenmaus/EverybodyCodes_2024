with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    r = [p for p in r if p in maze]
    return r


start = None
maze = set()
herbs = set()
for y in range(len(lines)):
    for x in range(len(lines[0])):
        p = (x, y)
        c = lines[y][x]
        match c:
            case "H":
                herbs.add(p)
                maze.add(p)
            case ".":
                maze.add(p)
                if start is None:
                    start = p

open = {start}
done = set()
steps = 0
while not any([h in open for h in herbs]):
    steps += 1
    done |= open
    next = set()
    for o in open:
        for n in get_all_nei(o):
            if n not in done:
                next.add(n)
    open = next

print(steps * 2)
