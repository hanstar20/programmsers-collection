import itertools

def solution(nums):
    answer = 0
    Num =[]
    nCr = itertools.combinations(nums, 3)
    
    for i in nCr:
        Num.append(sum(i))
    
    for i in Num:
        price_number = True
        if i != 1:
            for j in range(2,i):
                if i % j == 0:
                    price_number = False
            if price_number:
                answer += 1
            
    return answer