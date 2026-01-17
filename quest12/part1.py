with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]


def req_power(dx, dy):
    if dy == 0:
        if dx % 3 == 0:
            return dx // 3
    elif dy > 0:
        if (dx - dy) % 3 == 0:
            return (dx - dy) // 3
    elif dy < 0:
        if -dy == dx:
            return dx
        elif -dy < dx:
            for power in range(dx // 3, dx):
                if dx <= 2 * power:
                    if -dy == power:
                        return power
                elif dx <= 3 * power:
                    offset = dx - 2 * power
                    if power - offset == -dy:
                        return power
    return None


X = len(lines[0])
Y = len(lines)

points = {"A": 1, "B": 2, "C": 3}

targets = set()
knights = set()
for y in range(Y):
    for x in range(X):
        p = (x, y)
        c = lines[y][x]
        if c == "T":
            targets.add(p)
        if c in "ABC":
            knights.add(p)

result = 0
for target in sorted(targets):
    tx, ty = target
    for k in knights:
        kx, ky = k
        dy = ty - ky
        dx = tx - kx
        res = req_power(dx, dy)
        if res is not None:
            result += res * points[lines[ky][kx]]
            break

print(result)
