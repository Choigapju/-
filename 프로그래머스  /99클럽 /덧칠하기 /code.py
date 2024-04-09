def solution(n, m, section):
    answer = 0
    tmp = 0
    for i in range(len(section)):
        if section[i] <= tmp:
            continue
            
        else:
            answer += 1
            tmp = section[i] + m -1
    
    return answer
