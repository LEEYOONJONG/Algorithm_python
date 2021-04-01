n, k = map(int, input().split())

arr=[]
for _ in range(n):
    tmp = int(input())
    arr.append(tmp)

count=0
for i in range(n-1, -1, -1):
    if k >= arr[i]:
        moks = k//arr[i]
        k -= arr[i]*moks
        count += moks
    

print(count)