def solution(k, ranges):
    sequence = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3 * k + 1
        sequence.append(k)

    n = len(sequence)
    area = [0] * n
    for i in range(1, n):
        area[i] = area[i-1] + (sequence[i-1] + sequence[i]) / 2

    answer = []
    for x, y in ranges:
        if x >= n + y:
            answer.append(-1.0)
        else:
            if y == 0:
                result = area[n-1] - area[x]
            else:
                result = area[n+y-1] - area[x]
            answer.append(result)

    return answer
