with open('day2/day2_input.txt') as f:
    guide = [r.lower().split(' ') for r in f.read().split('\n')]

outcomes = {'a': {'x': 3, 'y': 6, 'z': 0},
            'b': {'x': 0, 'y': 3, 'z': 6},
            'c': {'x': 6, 'y': 0, 'z': 3}
            }

moves = {'x': 1, 'y': 2, 'z': 3}

score = 0

for i, j in guide:
    score += outcomes[i][j]
    score += moves[j]

print("The score for Part 1 is:", score)

p2score = 0

p2outcomes = {'a': {'x': 3, 'y': 4, 'z': 8},
              'b': {'x': 1, 'y': 5, 'z': 9},
              'c': {'x': 2, 'y': 6, 'z': 7}
              }

for i, j in guide:
    p2score += p2outcomes[i][j]

print("The score for Part 2 is:", p2score)