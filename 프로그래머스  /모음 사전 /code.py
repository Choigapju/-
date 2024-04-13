def solution(word):
    answer = 0
    alphabets = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    length = len(word)

    for i in range(length):
        for j in range(5 - i):
            answer += alphabets[word[i]] * (5 ** j)
        answer += 1

    return answer
