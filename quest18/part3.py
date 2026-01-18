import functools

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


@functools.cache
def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    r = [p for p in r if p in maze]
    return r


@functools.cache
def bfs(start):
    open = {start}
    distances = {start: 0}
    d = 0
    while distances.keys() != maze:
        d += 1
        next_open = set()
        for o in open:
            for n in get_all_nei(o):
                if n not in distances:
                    distances[n] = d
                    next_open.add(n)
        open = next_open
    return distances


@functools.cache
def distance(p, q):
    return bfs(p)[q]


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

opt = 2 ** 32
for p in maze:
    if p not in palms:
        opt = min(opt, sum([distance(q, p) for q in palms]))
print(opt)
