def solution(board, moves):
    answer = 0
    N = len(board)
    hook = 0
    basket = []
    for move in moves:
        for i in range(N):
            if board[i][move-1] != 0:
                print(board[i][move-1])
                hook = board[i][move-1]
                board[i][move-1] = 0
                break
        if hook != 0:
            if len(basket) == 0 or basket[-1] != hook:
                basket.append(hook)
                hook = 0
            elif basket[-1] == hook:
                basket.pop(-1)
                hook = 0
                answer += 2
        
    
    return answer