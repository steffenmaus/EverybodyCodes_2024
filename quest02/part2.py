with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

words, text = lines[0], lines[2:]

words = words.split(":")[1].split(",")

symbol = set()

for j in range(len(text)):
    line = text[j]
    for i in range(len(line)):
        for w in words:
            if line[i:].startswith(w) or line[i:].startswith(w[::-1]):
                for x in range(len(w)):
                    symbol.add((i + x, j))

print(len(symbol))
