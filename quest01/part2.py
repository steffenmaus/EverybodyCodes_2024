with open('input2.txt') as file:
    lines = [line.rstrip() for line in file]

creatures = lines[0]
potions = 0

for i in range(0, len(creatures), 2):
    current = creatures[i:i + 2]
    real_monsters = 0
    for c in current:
        if c in list("ABCD"):
            real_monsters += 1
        match c:
            case "B":
                potions += 1
            case "C":
                potions += 3
            case "D":
                potions += 5
    if real_monsters == 2:
        potions += 2

print(potions)
