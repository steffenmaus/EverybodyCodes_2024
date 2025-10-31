with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

nails = [int(l) for l in lines]
target = sorted(nails)[len(nails)//2]
out = 0
for n in nails:
    out += abs(n - target)
print(out)