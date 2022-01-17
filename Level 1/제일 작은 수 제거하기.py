def solution(arr):
    answer = []
    arr.remove(min(arr))
    if arr == []:
        answer = [-1]
    else:
        answer = arr
    return answer