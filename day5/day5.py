import copy

with open('day5/day5_input.txt') as f:
    start = f.readlines()[0:8]
    start = [line[1::4] for line in start]
with open('day5/day5_input.txt') as f:
    instructions = f.readlines()[10:]
    instructions = [line.replace("\n", "") for line in instructions]

stacks1 = {i:[] for i in range(1,10)}
stacks2 = {i:[] for i in range(1,10)}

for row in start[::-1]:
    letters = [l for l in row]
    for i in range(1, 10):
        if letters[i-1] != ' ':
         stacks1[i].append(letters[i-1])
         stacks2[i].append(letters[i-1])

steps = []

for line in instructions:
    m = int(line.split()[1])
    f = int(line.split()[3])
    t = int(line.split()[5])
    steps.append([m, f, t])

for m, f, t in steps:
    for i in range(m):
        stacks1[t].append(stacks1[f].pop())

part1 = []
for i in range(1, 10):
    part1.append(stacks1[i][-1])

# part 2

for m, f, t in steps:
    stacks2[t].extend(stacks2[f][-m:])
    stacks2[f] = stacks2[f][:-m]

part2 = []
for i in range(1, 10):
    part2.append(stacks2[i][-1])

print("Part 1 answer is:", part1)
print("Part 2 answer is:", part2)