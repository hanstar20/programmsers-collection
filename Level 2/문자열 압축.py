def solution(s):
    answer = 0
    min_len = []
    # 우선 길이별로 나눠야함
    for length in range(1, len(s) + 1):
        word = ''
        temp_word = []
        for i in range(0, len(s), length):
            if i + length > len(s):
                temp_word.append(s[i:])
            else:
                temp_word.append(s[i:i + length])

        overlap = 1
        for idx in range(len(temp_word)):
            if idx != len(temp_word) - 1:
                if temp_word[idx] == temp_word[idx+1]:
                    overlap += 1
                else:
                    if overlap == 1:
                        word += temp_word[idx]
                    else:
                        word += str(overlap) + temp_word[idx]
                        overlap = 1

            else:
                if overlap == 1:
                    word += temp_word[idx]
                else:
                    word += str(overlap) + temp_word[idx]

        min_len.append(len(word))

    answer = min(min_len)
    return answer

