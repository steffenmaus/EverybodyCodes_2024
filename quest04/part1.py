with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

nails = [int(l) for l in lines]
target = min(nails)
out = 0
for n in nails:
    out += abs(n - target)
print(out)