from collections import defaultdict
from itertools import permutations

with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


def f(x, y, path):
    if (x, y) == (0, 0):
        return path
    for x2, y2 in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
        if (x2, y2) != path[-1] and x2 in range(X) and y2 in range(Y) and lines[y2][x2] != " ":
            return f(x2, y2, path + [(x, y)])


Y = len(lines)
X = len(lines[0])
x, y = 0, 0

path = f(1, 0, [(0, 0)])
racetrack = "".join([lines[y][x] for x, y in path])
action = {'+': 1, '-': -1, '=': 0}
enemy = "+-++=+==+--"

plans = set(["".join(p) for p in permutations("+++++---===")])

powers = defaultdict(lambda: 10)
gathered = defaultdict(int)

track_pos = 1
plan_pos = 0
loop = 0
while loop < 11:  # shortcut: 11 is divisor of 2024
    match racetrack[track_pos]:
        case "+":
            for k in plans:
                new_val = powers[k] + 1
                powers[k] = new_val
                gathered[k] += new_val
        case "-":
            for k in plans:
                new_val = max(0, powers[
                    k] - 1)  # if new_val would actually become 0 once, the shortcut would be incorrect.
                powers[k] = new_val
                gathered[k] += new_val
        case _:
            for k in plans:
                new_val = max(0, powers[k] + action[k[plan_pos]])  # see comment above
                powers[k] = new_val
                gathered[k] += new_val

    track_pos += 1
    track_pos %= len(racetrack)
    if track_pos == 1:
        loop += 1
    plan_pos += 1
    plan_pos %= 11

out = len([x for x in gathered if gathered[x] > gathered[enemy]])
print(out)
