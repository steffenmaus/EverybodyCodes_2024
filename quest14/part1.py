with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

y = 0
max_height = 0
for instr in lines[0].split(","):
    d = instr[0]
    steps = int(instr[1:])
    if d == "U":
        y += steps
    elif d == "D":
        y -= steps
    max_height = max(y, max_height)

print(max_height)
