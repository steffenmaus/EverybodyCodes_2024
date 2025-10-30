with open('input1.txt') as file:
    lines = [line.rstrip() for line in file]

creatures = lines[0]
potions = 0

for c in creatures:
    match c:
        case "B":
            potions += 1
        case "C":
            potions += 3
        case "D":
            potions += 5

print(potions)
