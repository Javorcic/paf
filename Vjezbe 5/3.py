import math

pod = [2.3, 4.5, 3.1, 5.7, 6.2, 1.8, 4.9, 3.6, 5.1, 2.7]
n = len(pod)

mean = sum(pod) / n

std = math.sqrt(sum((x - mean) ** 2 for x in pod) / (n * (n - 1)))

print("podatci:", pod)
print(f"n = {n}")
print(f"Mean = {mean:.4f}")
print(f"Std dev = {std:.4f}")