def solution(sequence, k):
    answer = []
    start = 0
    end = 0
    current_sum = 0
    min_length = float('inf')
    
    while end < len(sequence):
        current_sum += sequence[end]
        
        while current_sum >= k:
            if current_sum == k:
                length = end - start + 1
                if length < min_length:
                    min_length = length
                    answer = [start, end]
                    
            current_sum -= sequence[start]
            start += 1
        end += 1
    return answer
