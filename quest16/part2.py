import functools
from collections import Counter
from collections import defaultdict

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]


@functools.cache
def calc_score(pos):
    score = 0
    symbols = "".join([wheels[w][p][0] + wheels[w][p][2] for w, p in enumerate(pos)])
    for c in Counter(symbols).items():
        if c[1] >= 3:
            score += c[1] - 2
    return score


positions = list(map(int, lines[0].split(",")))

wheels = defaultdict(list)
for line in lines[2:]:
    for i in range(0, len(line), 4):
        part = line[i:i + 3]
        if part != "   ":
            wheels[i // 4].append(part)

pos = [0] * len(positions)

coins = 0
total_steps_required = 202420242024
steps = 0
state_at = {}
value_at = {}
while steps < total_steps_required:
    state = tuple(pos)
    if state in state_at:
        loop_size = steps - state_at[state]
        value_diff_per_loop = coins - value_at[state]
        full_loops_to_skip = (total_steps_required - steps) // loop_size
        coins += full_loops_to_skip * value_diff_per_loop
        steps += full_loops_to_skip * loop_size
        if steps == total_steps_required:
            break
    else:
        state_at[state] = steps
        value_at[state] = coins
    steps += 1

    next_pos = []
    for i, p in enumerate(pos):
        next_pos.append((p + positions[i]) % len(wheels[i]))
    pos = next_pos
    coins += calc_score(tuple(pos))

print(coins)
