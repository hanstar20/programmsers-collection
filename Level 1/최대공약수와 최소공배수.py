def solution(n, m):
    answer = []
    lmc = n * m
    while True:
        r = max(n, m) % min (n, m)
        if r == 0:
            gcd = min(n, m)
            break
        n = min(n, m)
        m = r
    
    lmc = lmc / gcd
    
    answer = [gcd, lmc]
    return answer