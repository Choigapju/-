# N, M, K 공백으로 구분하여 입력 받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬
first = data[-1]
second = data[-2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 while 탈출
            break
        result += first
        m -= 1
        
    if m == 0: # m이 0이라면 반복 탈출
        break
    
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1
    
print(result)
