with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

words, text = lines[0], lines[2]

words = words.split(":")[1].split(",")

out = 0

for i in range(len(text)):
    for w in words:
        if text[i:].startswith(w):
            out += 1

print(out)
