import math

def solution(n):
    answer = '수박' * math.ceil(n/2)
    if n % 2 == 1:
        answer = answer[:-1]
    return answer