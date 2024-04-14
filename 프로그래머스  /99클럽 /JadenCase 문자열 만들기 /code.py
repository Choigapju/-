def solution(s):
    temp = s.split(' ')
    answer = []
    
    for i in temp:
        i = i.capitalize()
        answer.append(i)
        
    return ' '.join(answer)
