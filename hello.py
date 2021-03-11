





n, a, b = map(int, input().split())
# print(n, a, b)

ca, cb = min(a, b), max(a, b)
count=1
while(True):
    if cb==ca+1 and ca%2==1: # 연속된 수이고, 앞의 수가 홀수라면
        break
    count += 1
    ca = (ca+1)//2
    cb = (cb+1)//2


    
print(count)