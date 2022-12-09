with open('day2/day2_input.txt') as f:
    guide = [r.replace(" ", "") for r in f.read().split('\n')]

scores = {'AX': 4,
          'AY': 8,
          'AZ': 3,
          'BX': 1,
          'BY': 5,
          'BZ': 9,
          'CX': 7,
          'CY': 2,
          'CZ': 6
          }

final = 0

for r in guide:
    final += scores[r]

print(final)