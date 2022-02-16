largest = 1

# brute force
for a in range(1, 100):
    for b in range(1, 100):
        list = map(int, str(a**b))
        total = sum(list)
        if total > largest:
            largest = total

print(largest)