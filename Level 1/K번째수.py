def solution(array, commands):
    answer = []
    
    for _list in (commands):
        temp = array[_list[0]-1:_list[1]]
        temp.sort()
        answer.append(temp[_list[2]-1])
    
    return answer