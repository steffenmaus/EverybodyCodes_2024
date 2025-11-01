from collections import defaultdict

with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

action = {'+': 1, '-': -1, '=': 0}
plans = {}
for l in lines:
    k, v = l.split(":")
    plans[k] = v.split(",")

powers = defaultdict(lambda: 10)
gathered = defaultdict(int)

for segment in range(10):
    for k in plans:
        new_val = max(0, powers[k] + action[plans[k][segment % len(plans[k])]])
        powers[k] = new_val
        gathered[k] += new_val

plans_sorted = sorted(gathered.items(), key=lambda x: x[1], reverse=True)
out = "".join([x[0] for x in plans_sorted])
print(out)
