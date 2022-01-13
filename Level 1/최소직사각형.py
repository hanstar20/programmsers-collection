def solution(sizes):
    answer = 0
    weight = 0
    height = 0
    for size in sizes:
        if size[0] < size[1]:
            weight = max(weight, size[1])
            height = max(height, size[0])
        else :
            weight = max(weight, size[0])
            height = max(height, size[1])
    
    answer = weight * height
    return answer