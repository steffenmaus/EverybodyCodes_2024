from collections import defaultdict

with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

root = "RR"
children = defaultdict(list)
powers = defaultdict(list)

for l in lines:
    k, v = l.split(":")
    children[k] = v.split(",")


def f(node, path, depth):
    for c in children[node]:
        if c == "@":
            powers[depth].append(path + "@")
        else:
            f(c, path + c[0], depth + 1)


f(root, root[0], 0)

ans = [p for p in powers.values() if len(p) == 1][0][0]
print(ans)
