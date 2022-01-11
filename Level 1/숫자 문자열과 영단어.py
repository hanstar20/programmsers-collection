def solution(s):
    answer = 0
    
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, word in enumerate(words):
        s = s.replace(word, str(idx))

    answer = int(s)
    return answer