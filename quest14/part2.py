with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

dirs = {"U": (0, 1, 0), "D": (0, -1, 0), "R": (1, 0, 0), "L": (-1, 0, 0), "F": (0, 0, 1), "B": (0, 0, -1)}

segments = set()

for line in lines:
    x, y, z = 0, 0, 0
    for instr in line.split(","):
        dx, dy, dz = dirs[instr[0]]
        for _ in range(int(instr[1:])):
            x += dx
            y += dy
            z += dz
            segments.add((x, y, z))

print(len(segments))
