with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

next_gen = {}
for line in lines:
    a, b = line.split(":")
    next_gen[a] = b.split(",")

open = ["Z"]
for _ in range(10):
    next_open = []
    for o in open:
        for n in next_gen[o]:
            next_open.append(n)
    open = next_open

print(len(open))
