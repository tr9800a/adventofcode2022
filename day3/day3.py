def prioritize(l):
    if l.islower():
        return (ord(l) - 96)
    else:
        return (ord(l) - 38)

def split(s):
    l = int(.5 * len(s))
    p1 = s[l:]
    p2 = s[:l]
    return [p1, p2]

with open('day3/day3_input.txt') as f:
    sacks = [split([prioritize(l) for l in s]) for s in f.read().split('\n')]

priority1 = 0

for s1, s2 in sacks:
    p = list(set(s1) & set(s2))
    priority1 += p[0]

print("Part 1's answer is:", priority1)

# part 2

with open('day3/day3_input.txt') as f:
    sacks2 = [[prioritize(l) for l in s] for s in f.read().split('\n')]

teams = [[x, y, z] for x, y, z in zip(sacks2[0::3], sacks2[1::3], sacks2[2::3])]

priority2 = 0

for x, y, z in teams:
    p2 = list(set(x) & set(y) & set(z))
    priority2 += p2[0]

print("Part 2's answer is:", priority2)