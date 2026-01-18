import functools

from collections import Counter

from collections import defaultdict

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


@functools.cache
def calc_score(pos):
    score = 0
    symbols = "".join([wheels[w][p][0] + wheels[w][p][2] for w, p in enumerate(pos)])
    for c in Counter(symbols).items():
        if c[1] >= 3:
            score += c[1] - 2
    return score


@functools.cache
def f(pos, remaining):
    if remaining == 0:
        return 0, 0
    scores = set()
    for offset in (-1, 0, 1):
        next_pos = []
        for i, p in enumerate(pos):
            next_pos.append((p + positions[i] + offset) % len(wheels[i]))
        next_pos = tuple(next_pos)
        delta_score = calc_score(next_pos)
        for v in f(next_pos, remaining - 1):
            scores.add(v + delta_score)
    return max(scores), min(scores)


positions = list(map(int, lines[0].split(",")))

wheels = defaultdict(list)
for line in lines[2:]:
    for i in range(0, len(line), 4):
        part = line[i:i + 3]
        if part != "   ":
            wheels[i // 4].append(part)

pos = [0] * len(positions)

print(" ".join([str(n) for n in f(tuple(pos), 256)]))
