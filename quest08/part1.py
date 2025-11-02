with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

blocks = int(lines[0])

w = 1
while blocks > 0:
    blocks -= w
    w += 2
w -= 2
print(blocks * w * -1)
