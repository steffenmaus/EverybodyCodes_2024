import heapq

with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

stars = set()
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "*":
            stars.add((x, y))

start = list(stars)[0]
Q = []
for s in stars:
    if s != start:
        d = abs(s[0] - start[0]) + abs(s[1] - start[1])
        heapq.heappush(Q, (d, s))

total = 0
done = {start}
while done != stars:
    d, s = heapq.heappop(Q)
    if s not in done:
        total += d
        done.add(s)
        for t in stars - done:
            d = abs(s[0] - t[0]) + abs(s[1] - t[1])
            heapq.heappush(Q, (d, t))

print(total + len(stars))
