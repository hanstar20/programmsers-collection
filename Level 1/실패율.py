def solution(N, stages):
    answer = []
    failRateDict = {}
    users = len(stages)
    
    for i in range(1, N+1):
        failCnt = stages.count(i)
        failRate = 0
        
        if failCnt != 0:
            failRate = failCnt / users
        
        failRateDict[i] = failRate
        users -= failCnt
    answer = sorted(failRateDict, key=lambda x: failRateDict[x], reverse=True)
    
    return answer