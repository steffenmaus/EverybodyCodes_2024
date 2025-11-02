with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

high_priests = int(lines[0])
blocks = 202400000
acolytes = 10

w = 1
thickness = 1
blocks -= 1
heights = [1]
while blocks > 0:
    w += 2
    thickness *= high_priests
    thickness %= acolytes
    thickness += acolytes
    heights.append(thickness)
    blocks -= w * thickness

for i in range(1, len(heights) - 1):
    blocks += 2 * (((high_priests * w) * sum(heights[i:])) % acolytes)
blocks += ((high_priests * w) * sum(heights)) % acolytes

print(-1 * blocks)
