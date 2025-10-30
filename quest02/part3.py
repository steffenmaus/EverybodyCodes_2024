with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

words, grid = lines[0], lines[2:]

words = words.split(":")[1].split(",")

Y = len(grid)
X = len(grid[0])

symbols = set()


def f(x, y, dx, dy, path, remaining):
    if not remaining:
        symbols.update(path)
        return True
    if y not in range(Y):
        return False
    if grid[y][x] == remaining[0]:
        return f((x + dx) % X, y + dy, dx, dy, path + [(x, y)], remaining[1:])
    return False


for x in range(X):
    for y in range(Y):
        for w in words:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                f(x, y, dx, dy, [], w)

print(len(symbols))
