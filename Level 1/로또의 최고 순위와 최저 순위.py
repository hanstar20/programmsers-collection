def solution(lottos, win_nums):
    answer = []
    grade = {'0' : 6, '1' : 6, '2' : 5, '3' : 4, '4' : 3, '5' : 2, '6' : 1}
    correct = 0
    unknown = 0
    
    for win_num in win_nums:
        if win_num in lottos:
            correct += 1
    
    unknown = lottos.count(0)
    
    max_result = grade[str(correct + unknown)]
    min_result = grade[str(correct)]
    
    answer = [max_result, min_result]
    
    return answer