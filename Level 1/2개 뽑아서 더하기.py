from itertools import combinations

def solution(numbers):
    answer = []
    com_numbers = list(combinations(numbers,2))
    
    for num1, num2 in com_numbers:
        if num1 + num2 not in answer:
            answer.append(num1 + num2)
    
    answer.sort()
    
    return answer