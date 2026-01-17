import heapq

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    r = [p for p in r if p in maze]
    return r


def get_dist(a, b):
    a, b = sorted([a, b])
    if b - a <= 5:
        return b - a + 1
    return a + 10 - b + 1


def dijkstra(start):
    out = {start: 0}
    Q = []
    for node in get_all_nei(start):
        heapq.heappush(Q, (maze[node] + 1, node))
    while Q:
        dist, current = heapq.heappop(Q)
        if current not in out:
            out[current] = dist
            for n in get_all_nei(current):
                heapq.heappush(Q, (get_dist(maze[current], maze[n]) + dist, n))
    return out


X = len(lines[0])
Y = len(lines)

maze = {}
start = None
target = None
for y in range(Y):
    for x in range(X):
        p = (x, y)
        c = lines[y][x]
        if c.isnumeric():
            maze[p] = int(c)
        elif c == "S":
            start = p
            maze[p] = 0
        elif c == "E":
            target = p
            maze[p] = 0

print(dijkstra(start)[target])
