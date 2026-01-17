with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]


# caution: positive y == downwards
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


flakes = set()  # positive y == upwards
for line in lines:
    x, y = line.split(" ")
    flakes.add((int(x), int(y)))

knights = set()
for y in range(3):
    knights.add((0, y))

result = 0
for target in flakes:
    tx, ty = target
    if tx % 2 != 0:
        tx -= 1
        ty -= 1
    tx = tx // 2
    ty -= tx
    candidates = set()
    for k in knights:
        kx, ky = k
        dy = ty - ky
        dx = tx - kx
        res = req_power(dx, -dy)  # flipped y!
        if res is not None:
            candidates.add(res * (ky + 1))
    result += min(candidates)

print(result)
