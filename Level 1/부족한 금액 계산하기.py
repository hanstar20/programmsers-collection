def solution(price, money, count):
    answer = -1
    full_price = 0
    
    for i in range(1, count+1):
        full_price += i * price
    
    if full_price <= money:
        answer = 0
    else:
        answer = full_price - money
    
    return answer