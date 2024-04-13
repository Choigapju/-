from itertools import product

def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    for i in range(1,6):
        words.extend(list(product(alphabets, repeat=i)))
    
    words = [''.join(word) for word in words]
    words.sort()
    
    return words.index(word) + 1
