def solution(s, skip, index):
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
    for char in skip:
        alphabet.remove(char)
    
    result = ""
    
    for char in s:
        idx = alphabet.index(char) + index
        idx %= len(alphabet)
        
        result += alphabet[idx]
    
    return result
