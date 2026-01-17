import functools
import heapq
from collections import defaultdict

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]


@functools.cache
def get_all_nei(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    r = [p for p in r if p in maze]
    return r


@functools.cache
def dijkstra(start):
    out = {start: 0}
    Q = []
    for node in get_all_nei(start):
        heapq.heappush(Q, (1, node))
    while Q:
        dist, current = heapq.heappop(Q)
        if current not in out:
            out[current] = dist
            for n in get_all_nei(current):
                heapq.heappush(Q, (1 + dist, n))
    return out


@functools.cache
def distance(p, q):
    return dijkstra(p)[q]


@functools.cache
def f(current, remaining):
    if len(remaining) == 0:
        return distance(current, start)
    out = 10 ** 32
    for r in remaining:
        next_remaining = frozenset(remaining - {r})
        for n in herbs[r]:
            step = distance(current, n)
            if step <= STEP_SIZE_LIMIT:
                out = min(out, step + f(n, next_remaining))

    return out

STEP_SIZE_LIMIT = 200

start = None
maze = set()
herbs = defaultdict(list)
for y in range(len(lines)):
    for x in range(len(lines[0])):
        p = (x, y)
        c = lines[y][x]
        match c:
            case "#":
                None
            case "~":
                None
            case ".":
                maze.add(p)
                if start is None:
                    start = p
            case _:
                herbs[c].append(p)
                maze.add(p)

print(f(start, frozenset(herbs.keys())))
