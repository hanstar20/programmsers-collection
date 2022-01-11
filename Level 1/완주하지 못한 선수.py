def solution(participant, completion):
    d = dict()
    for person in participant:
        d[person] = d.get(person, 0) + 1
    for person in completion:
        d[person] -= 1

    return list(key for key, val in d.items() if val == 1).pop()