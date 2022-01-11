def solution(nums):
    answer = 0
    max_answer = len(set(nums))
    pick = len(nums)//2
    if max_answer >= pick:
        answer = pick
    else:
        answer = max_answer
    return answer