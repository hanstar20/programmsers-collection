def solution(s):
    answer = True
    s_p = 0
    s_y = 0
    
    for string in s:
        if string == 'p' or string == 'P':
            s_p += 1
        
        if string == 'y' or string == 'Y':
            s_y += 1
        

    if s_p != s_y:
        answer = False

    return answer