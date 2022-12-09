with open('day1/day1_input.txt') as f:
    text = [p.strip() for p in f.read().split('\n\n')]

elves = [e.split('\n') for e in text]

elves_int = [list(map(int, elf)) for elf in elves]

elf_totals = [sum(cal) for cal in elves_int]

elf_totals.sort()

print("Part one's answer is:", elf_totals[-1])
print("Part two's answer is:", sum(elf_totals[-3:]))