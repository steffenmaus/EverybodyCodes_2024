import functools

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


@functools.cache
def f(current, remaining_depth):
    if remaining_depth == 0:
        return 1
    count = 0
    for n in next_gen[current]:
        count += f(n, remaining_depth - 1)
    return count


next_gen = {}

for line in lines:
    a, b = line.split(":")
    next_gen[a] = b.split(",")

counts = set()
for k in next_gen:
    counts.add(f(k, 20))

print(max(counts) - min(counts))
