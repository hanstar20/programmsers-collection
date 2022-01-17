from collections import deque

def solution(progresses, speeds):
    answer = []
    deque_progresses = deque(progresses)
    deque_speeds = deque(speeds)
    temp = 0

    while True:
        if len(deque_progresses) == 0:
            break
        # 1일 지날 때 진행량 추가
        for i in range(len(deque_progresses)):
            deque_progresses[i] += deque_speeds[i]

        while True:
            if deque_progresses[0] >= 100:
                temp += 1
                deque_progresses.popleft()
                deque_speeds.popleft()
                if len(deque_progresses) == 0:
                    answer.append(temp)
                    temp = 0
                    break
            else:
                if temp != 0:
                    answer.append(temp)
                temp = 0
                break

    return answer