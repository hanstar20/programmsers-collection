def solution(seoul):
    for idx, people in enumerate(seoul):
        if people == 'Kim':
            return f'김서방은 {idx}에 있다'