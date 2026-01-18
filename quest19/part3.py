with open('input3.txt') as file:
    lines = [line.rstrip() for line in file]

operations = lines[0]
lines = lines[2:]
OUTER_COORDS = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

X = len(lines[0])
Y = len(lines)


def rotate(p, op, matrix):
    x, y = p
    outer = []
    for dx, dy in OUTER_COORDS:
        outer.append(matrix[(x + dx, y + dy)])

    step = 1
    if op == "R":
        step = -1

    for i in range(8):
        dx, dy = OUTER_COORDS[i]
        matrix[x + dx, y + dy] = outer[(i + step) % 8]


def get_rotation_matrix():
    matrix = {}
    for y in range(Y):
        for x in range(X):
            matrix[(x, y)] = (x, y)
    pos = 0
    for y in range(1, Y - 1):
        for x in range(1, X - 1):
            op = operations[pos]
            rotate((x, y), op, matrix)
            pos += 1
            pos %= len(operations)
    return matrix


def matrix_multiply(m, n):
    out = {}
    for p in m:
        out[p] = n[m[p]]
    return out


# https://en.wikipedia.org/wiki/Exponentiation_by_squaring
def exp_by_squaring(matrix, n):
    if n == 1:
        return matrix
    if n % 2 == 0:
        return exp_by_squaring(matrix_multiply(matrix, matrix), n // 2)
    else:
        return matrix_multiply(matrix, exp_by_squaring(matrix_multiply(matrix, matrix), (n - 1) // 2))


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


rotation = exp_by_squaring(get_rotation_matrix(), 1048576000)

decrypted = {}
for p_final, p_origin in rotation.items():
    decrypted[p_final] = lines[p_origin[1]][p_origin[0]]

print(extract_result(decrypted))
