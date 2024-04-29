def solution(today, terms, privacies):
    term_dict = {i.split()[0] : int(i.split()[1]) * 28 for i in terms}
    
    YYYY, MM, DD = map(int, today.split('.'))
    today_int = YYYY * 12 * 28 + MM * 28 + DD # 오늘날짜 정수화
    
    answer = []
    
    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        year, month, day = map(int, date.split('.'))
        
        limit = year * 12 * 28 + month * 28 + day + term_dict[term]
        
        if limit <= today_int:
            answer.append(i+1)
            
    return answer
