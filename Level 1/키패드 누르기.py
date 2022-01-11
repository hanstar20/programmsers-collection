def solution(numbers, hand):
    answer = ''
    keypads = [["1","2","3"], ["4","5","6"], ["7","8","9"],["*", "0" ,"#"]]
    left = "*"
    right = "#"

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left = str(number)

        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right = str(number)

        else:
            right_idx = [(i,j) for i in range(4) for j in range(3) if keypads[i][j] == right]
            left_idx = [(i,j) for i in range(4) for j in range(3) if keypads[i][j] == left]
            number_idx = [(i,j) for i in range(4) for j in range(3) if keypads[i][j] == str(number)]
            right_dis = abs(right_idx[0][0] - number_idx[0][0]) + abs(right_idx[0][1] - number_idx[0][1])
            left_dis = abs(left_idx[0][0] - number_idx[0][0]) + abs(left_idx[0][1] - number_idx[0][1])

            if right_dis > left_dis:
                answer += 'L'
                left = str(number)
            elif right_dis < left_dis:
                answer += 'R'
                right = str(number)
            elif right_dis == left_dis:
                if hand == "right":
                    answer += 'R'
                    right = str(number)
                elif hand == "left":
                    answer += 'L'
                    left = str(number)
        
    return answer