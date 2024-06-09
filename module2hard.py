def find_pairs(n):
    pairs = []
    used_numbers = set()

    for i in range(1, n):
        for j in range(i + 1, n):
            if i not in used_numbers and j not in used_numbers and n % (i + j) == 0:
                pairs.append((i, j))
                used_numbers.add(i)
                used_numbers.add(j)

    return pairs

def create_password(pairs):
    password = ''
    for pair in pairs:
        password += str(pair[0]) + str(pair[1])
    return password

numbers = list(range(3, 21))
for n in numbers:
    pairs = find_pairs(n)
    result = create_password(pairs)
    print(f"{n}", "-", (result))