n, m = map(int, input().split())
mylist=[]
for i in range(n):
    mylist.append(list(input()))

k = int(input())

maximum=0

for i in range(n):
    zero=0
    for j in range(m):
        if mylist[i][j]=='0':
            zero += 1
    cnt=0
    if zero <= k and zero%2 == k%2:
        for j in range(n):
            if mylist[i]==mylist[j]:
                cnt+=1
    
    maximum = max(cnt, maximum)
    
print(maximum)