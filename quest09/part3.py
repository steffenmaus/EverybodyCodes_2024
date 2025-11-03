import sys

sys.setrecursionlimit(1000000)

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

cache = {}
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]


def f(n):
    if n in cache:
        return cache[n]

    candidates = [s for s in stamps if s <= n]
    if n in candidates:
        cache[n] = 1
        return 1

    pot = set()
    for c in candidates:
        pot.add(1 + f(n - c))
    cache[n] = min(pot)
    return min(pot)


total = 0
for l in lines:
    n = int(l)
    pot = set()
    for a in range((n // 2) - 50, (n // 2) + 51):
        b = n - a
        if abs(b - a) <= 100:
            pot.add(f(a) + f(b))
    total += min(pot)

print(total)
