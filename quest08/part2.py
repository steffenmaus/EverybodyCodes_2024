with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

priests = int(lines[0])
blocks = 20240000
acolytes = 1111

w = 1
thickness = 1
blocks -= 1
while blocks > 0:
    w += 2
    thickness *= priests
    thickness %= acolytes
    blocks -= w * thickness

print(-1 * w * blocks)
