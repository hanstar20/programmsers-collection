def solution(s):
    answer = ''
    strings = [x for x in s]
    strings.sort(reverse=True)
    for i in strings:
        answer += i
    return answer