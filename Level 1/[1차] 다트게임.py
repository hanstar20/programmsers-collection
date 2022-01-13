def solution(dartResult):
    answer = 0
    score = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    bonus = ['S', 'D', 'T']
    option = ['*', '#']
    temp_score = ''
    result = []
    
    for i in dartResult:
        if i in score:
            temp_score += i
            
        elif i in bonus:
            if i == 'S':
                result.append(int(temp_score))
            elif i == 'D':
                result.append(int(temp_score)**2)
            elif i == 'T':
                result.append(int(temp_score)**3)
                
            temp_score = ''
            
        elif i in option:
            if i ==  '*':
                result[-1] = result[-1] * 2
                if len(result) != 1:
                    result[-2] = result[-2] * 2
                    
            elif i == '#':
                result[-1] = result[-1] * (-1)
        
            
        answer = sum(result)    
    
    return answer