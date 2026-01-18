import heapq
import math

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

stars = set()
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "*":
            stars.add((x, y))

sizes = []
done = set()
while done != stars:
    wide = 0
    count = 1
    start = list(stars - done)[0]
    done.add(start)
    Q = []
    for s in stars - done:
        d = abs(s[0] - start[0]) + abs(s[1] - start[1])
        if d < 6:
            heapq.heappush(Q, (d, s))
    while Q:
        d, s = heapq.heappop(Q)
        if s not in done:
            done.add(s)
            wide += d
            count += 1
            for t in stars - done:
                d = abs(s[0] - t[0]) + abs(s[1] - t[1])
                if d < 6:
                    heapq.heappush(Q, (d, t))
    sizes.append(wide + count)

print(math.prod(sorted(sizes)[-3:]))
