def solution(n):
    answer = 0
    num = sorted(list(map(str, str(n))), reverse=True)
    answer = int(''.join(num))
    return answer