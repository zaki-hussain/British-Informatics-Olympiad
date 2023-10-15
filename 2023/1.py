fibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]

n = int(input("Enter the number between 1 and 1,000,000 inclusive: "))

zeckendorf = []

for i in range(28, -1, -1):
    if n - fibonacci[i] >= 0:
        n -= fibonacci[i]
        zeckendorf.append(fibonacci[i])

print(zeckendorf)