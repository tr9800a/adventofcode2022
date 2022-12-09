with open('string.txt', 'r') as file:
    data = file.read()

letters = [x for x in data]

def packet(length):
    start = 0
    end = length
    answer = 0

    while answer == 0:
        if len(set(letters[start:end])) == length:
            answer = end
        else:
            start += 1
            end += 1
    return end

print("Part one's answer is:", packet(4))
print("Part two's answer is:", packet(14))