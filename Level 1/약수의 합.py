def solution(n):
    answer = 0
    
    divisors = []

    for i in range(1, int(n**(1/2)) + 1): 
        if (n % i == 0):            
            divisors.append(i)
            if (i != (n // i)): 
                divisors.append(n//i)
    
    set_divisors = set(divisors)
    answer = sum(set_divisors)
    
    return answer