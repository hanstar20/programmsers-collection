def solution(id_list, report, k):
    answer = []
    report_list = []
    black_list = []
    dict_id = {}
    for id in id_list:
        dict_id[id] = {'report_user' : [], 'report_num' : 0}

    for repo in set(report):
        report_list.append(repo.split(' '))

    for repo in report_list:
        # 신고자의 db에 신고한 사람 추가
        dict_id[repo[0]]['report_user'].append(repo[1])
        # 신고당한 사람 db에 신고당한 횟수 추가
        dict_id[repo[1]]['report_num'] += 1

    # 정지될 아이디 확인해서 black_list에 넣기
    for id in id_list:
        if dict_id[id]['report_num'] >= k:
            black_list.append(id)

    for id in id_list:
        answer.append(len(set(dict_id[id]['report_user']) & set(black_list)))

    return answer