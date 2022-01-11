def solution(answers):
    answer = []
    answer_1 = [1,2,3,4,5] * 2000
    answer_2 = [2,1,2,3,2,4,2,5] * 1430
    answer_3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    result = {1:0, 2:0, 3:0}
    
    answer_1 = answer_1[:len(answers)]
    answer_2 = answer_2[:len(answers)]
    answer_3 = answer_3[:len(answers)]
    
    for i in range(len(answers)):
        if answers[i] == answer_1[i]:
            result[1] += 1
        
        if answers[i] == answer_2[i]:
            result[2] += 1
        
        if answers[i] == answer_3[i]:
            result[3] += 1
    
    
    answer = [k for k,v in result.items() if max(result.values()) == v]

      
    
    return answer