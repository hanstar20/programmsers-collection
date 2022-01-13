def solution(n, arr1, arr2):
    answer = [''] * n
    sum_arr = []
    for i in range(n):
        sum_arr.append(arr1[i] | arr2[i])
    
    for idx, i in enumerate(sum_arr):
        for j in bin(i)[2:]:
            if j == '1':
                answer[idx] += '#'
            else:
                answer[idx] += ' '
    
    for idx, ans in enumerate(answer):
        if len(ans) != n:
            answer[idx] = ' '*(n-len(ans)) + answer[idx]
    
    return answer