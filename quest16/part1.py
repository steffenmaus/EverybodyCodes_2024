from collections import defaultdict

with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

positions = list(map(int, lines[0].split(",")))

wheels = defaultdict(list)
for line in lines[2:]:
    for i in range(0, len(line), 4):
        part = line[i:i + 3]
        if part != "   ":
            wheels[i // 4].append(part)

pos = [0] * len(positions)

res_pos = []
for i, p in enumerate(pos):
    res_pos.append((p + 100 * positions[i]) % len(wheels[i]))

print(" ".join([wheels[w][p] for w, p in enumerate(res_pos)]))
