with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

operations = lines[0]
lines = lines[2:]
OUTER_COORDS = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

X = len(lines[0])
Y = len(lines)


maze = {}
for y in range(Y):
    for x in range(X):
        p = (x, y)
        c = lines[y][x]
        maze[p] = c

def rotate(x, y, op):
    outer = []
    for dx, dy in OUTER_COORDS:
        outer.append(maze[(x + dx, y + dy)])

    step = 1
    if op == "R":
        step = -1

    for i in range(8):
        dx, dy = OUTER_COORDS[i]
        maze[x + dx, y + dy] = outer[(i + step) % 8]



def extract_result(decrypted):
    result = ""
    collect = False
    for _, c in sorted(decrypted.items(), key=lambda x: x[0][1]):
        if c == "<":
            return result
        elif collect:
            result += c
        elif c == ">":
            collect = True

for _ in range(100):
    pos = 0
    for y in range(1, Y - 1):
        for x in range(1, X - 1):
            op = operations[pos]
            rotate(x, y, op)
            pos += 1
            pos %= len(operations)

print(extract_result(maze))
