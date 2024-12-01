from collections import Counter

left = []
right = []

with open("input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

right_counter = Counter(right)

similarity_score = sum(left_value * right_counter[left_value] for left_value in left)

print(similarity_score)