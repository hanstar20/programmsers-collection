def solution(arr1, arr2):
    answer = []
    row = len(arr1)
    col = len(arr1[0])
    for i in range(row):
        answer.append([])
        for j in range(col):
            answer[i].append(arr1[i][j] + arr2[i][j])
        
    return answer