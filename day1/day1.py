left = []
right = []

with open("input.txt", "r") as file: 
    for line in file:
        parts = line.strip().split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

left.sort()
right.sort()


total_distance = sum(abs(l - r) for l, r in zip(left, right))

print(total_distance)