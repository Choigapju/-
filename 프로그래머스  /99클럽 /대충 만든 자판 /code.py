def solution(keymap, targets):
    answer = []
    alp_keys = dict()
    
    for words in keymap:
        for idx, alp in enumerate(words):
            if alp in alp_keys and (idx+1) > alp_keys[alp]:
                continue
                
            alp_keys[alp] = idx + 1
            
    for i in targets:
        total_index = 0
        
        for alp in i:
            if alp in alp_keys:
                total_index += alp_keys[alp]
                
            else:
                total_index = -1
                break
                
        answer.append(total_index)
        
    return answer
