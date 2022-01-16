a, b = map(int, input().strip().split(' '))
answer = ''
for _ in range(b):
    for _ in range(a):
        answer += '*'
    answer += '\n'
print(answer)