import string

def solution(s, n):
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    answer = ''
    for digit in s:
        if digit in lowercase:
            answer += lowercase[(lowercase.index(digit) + n) % 26]
        elif digit in uppercase:
            answer += uppercase[(uppercase.index(digit) + n) % 26]
        else:
            answer += ' '
    return answer