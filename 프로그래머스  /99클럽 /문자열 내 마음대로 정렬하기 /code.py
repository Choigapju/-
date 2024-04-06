def solution(strings, n):
    return sorted(strings, key=lambda x:(x[n],x))

# sort정렬과 lambda 함수로 풀이 해 보았음.
