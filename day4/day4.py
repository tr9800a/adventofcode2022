with open('day4/day4_input.txt') as f:
    pairs = [[[int(i) for i in n.split('-')] for n in p.split(',')] for p in f.read().split('\n')]

count = 0

for i, j in pairs:
    r1 = set(range(i[0], i[1] + 1))
    r2 = set(range(j[0], j[1] + 1))
    if r1.issubset(r2):
        count += 1
    elif r2.issubset(r1):
        count += 1

print(count, "assignments fully contained")

count2 = 0

for i, j in pairs:
    r1 = set(range(i[0], i[1] + 1))
    r2 = set(range(j[0], j[1] + 1))
    if r1.intersection(r2):
        count2 += 1
    elif r2.intersection(r1):
        count2 += 1

print(count2, "assignments overlapping")
