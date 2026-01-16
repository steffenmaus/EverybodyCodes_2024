import functools

with open('input3.txt') as file:
    lines = [list(line.rstrip()) for line in file]


def calc_power(word):
    out = 0
    for i, c in enumerate(word, 1):
        out += i * (ord(c) - 64)
    return out


@functools.cache
def is_solvable(offset):
    x_offset, y_offset = offset
    outer_horizontals = []
    for y in (0, 1, 6, 7):
        for x in range(2, 6):
            c = lines[y_offset + y][x_offset + x]
            if c != "?":
                outer_horizontals.append(c)
    if len(outer_horizontals) != len(set(outer_horizontals)):
        return False

    outer_verticals = []
    for y in range(2, 6):
        for x in (0, 1, 6, 7):
            c = lines[y_offset + y][x_offset + x]
            if c != "?":
                outer_verticals.append(c)
    if len(outer_verticals) != len(set(outer_verticals)):
        return False
    return True


def solve(offset):
    x_offset, y_offset = offset
    proceed = True
    while proceed:
        proceed = False
        for y in range(2, 6):
            for x in range(2, 6):
                if lines[y_offset + y][x_offset + x] == ".":
                    outer_horizontals = set([lines[y_offset + y][x_offset + x2] for x2 in (0, 1, 6, 7)])
                    inner_horizontals = set([lines[y_offset + y][x_offset + x2] for x2 in range(2, 6)]) - {"."}
                    outer_verticals = set([lines[y_offset + y2][x_offset + x] for y2 in (0, 1, 6, 7)])
                    inner_verticals = set([lines[y_offset + y2][x_offset + x] for y2 in range(2, 6)]) - {"."}
                    sol = (outer_horizontals & outer_verticals) - {"?"}
                    if len(sol) == 1:
                        proceed = True
                        lines[y_offset + y][x_offset + x] = sol.pop()
                    else:
                        if "?" in outer_horizontals and len(outer_horizontals) == 4:
                            if "?" not in outer_verticals and len(inner_verticals) == 3:
                                sol = (outer_verticals - inner_verticals).pop()
                                lines[y_offset + y][x_offset + x] = sol
                                proceed = True
                                for x2 in (0, 1, 6, 7):
                                    if lines[y_offset + y][x_offset + x2] == "?":
                                        lines[y_offset + y][x_offset + x2] = sol
                                        break
                        elif "?" in outer_verticals and len(outer_verticals) == 4:
                            if "?" not in outer_horizontals and len(inner_horizontals) == 3:
                                sol = (outer_horizontals - inner_horizontals).pop()
                                lines[y_offset + y][x_offset + x] = sol
                                proceed = True
                                for y2 in (0, 1, 6, 7):
                                    if lines[y_offset + y2][x_offset + x] == "?":
                                        lines[y_offset + y2][x_offset + x] = sol
                                        break
    word = ""
    for y in range(2, 6):
        for x in range(2, 6):
            word += lines[y_offset + y][x_offset + x]

    if "." in word:
        return None
    return word


offsets = set()
for y in range(0, len(lines) - 2, 6):
    for x in range(0, len(lines[0]) - 2, 6):
        offsets.add((x, y))

solved = {}

while offsets:
    next_offsets = set()
    for o in offsets:
        if is_solvable(o):
            res = solve(o)
            if res is not None:
                solved[o] = calc_power(res)
            else:
                next_offsets.add(o)
    offsets = next_offsets
print(sum(solved.values()))
