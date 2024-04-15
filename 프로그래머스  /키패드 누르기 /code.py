def solution(numbers, hand):
    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }
    l_hand = keypad['*']
    r_hand = keypad['#']
    answer = ''
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            l_hand = keypad[i]
        elif i in [3,6,9]:
            answer += 'R'
            r_hand = keypad[i]
        else:
            num_pos = keypad[i]
            l_dist = abs(num_pos[0] - l_hand[0]) + abs(num_pos[1] - l_hand[1])
            r_dist = abs(num_pos[0] - r_hand[0]) + abs(num_pos[1] - r_hand[1])
            
            if l_dist < r_dist:
                answer += 'L'
                l_hand = num_pos
            elif l_dist > r_dist:
                answer += 'R'
                r_hand = num_pos
            else:
                if hand == 'left':
                    answer += 'L'
                    l_hand = num_pos
                else:
                    answer += 'R'
                    r_hand = num_pos
                    
    return answer
