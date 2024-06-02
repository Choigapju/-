n, k = map(int, input().split())
cnt = 0

while n >= k: # n이 k이상이라면 k로 계속 나누기
    while n % k != 0: # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
        n -= 1
        cnt += 1

    n //= k # k로 나누기
    cnt += 1

while n > 1: # 마지막으로 남은 수에 대하여 1씩 빼기
    n -= 1
    cnt += 1

print(cnt)
