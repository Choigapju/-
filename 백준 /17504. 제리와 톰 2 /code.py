N = int(input())
A = list(map(int, input().split()))

A = A[::-1]
a, b = 1, 1

for i in range(len(A)):
    if i == 0:
        b = A[i]
        continue
    a = A[i] * b + a
    a, b = b, a
print(b - a, b)
