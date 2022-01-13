def solution(s):
    answer = ''
    odd = True
    
    for string in s:
        if string == ' ':
            odd = True
            answer += ' '
            continue
        
        if odd:
            answer += string.upper()
            odd = False
        else:
            answer += string.lower()
            odd = True
            
    return answer
