import functools
import heapq

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


@functools.cache
def get_all_nei(p):
    r = []
    x, y, z = p
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                if abs(dx) + abs(dy) + abs(dz) == 1:
                    r.append((x + dx, y + dy, z + dz))
    r = [p for p in r if p in segments]
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


dirs = {"U": (0, 1, 0), "D": (0, -1, 0), "R": (1, 0, 0), "L": (-1, 0, 0), "F": (0, 0, 1), "B": (0, 0, -1)}

segments = set()
leafs = set()
for line in lines:
    x, y, z = 0, 0, 0
    for instr in line.split(","):
        p = x, y, z
        dx, dy, dz = dirs[instr[0]]
        for _ in range(int(instr[1:])):
            x += dx
            y += dy
            z += dz
            segments.add((x, y, z))
    leafs.add((x, y, z))

opt = 2 ** 32
for s in segments:
    if s[0] == 0 and s[2] == 0:
        total = 0
        for leaf in leafs:
            total += dijkstra(leaf)[s]
        opt = min(total, opt)

print(opt)
