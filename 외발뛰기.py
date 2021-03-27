
def jump(row, col, n):
    global cache # 0이면 없음, 1이면 존재
    global arr

    if (row>=n or col >=n): # 넘어가면
        return 0

    if cache[row][col] != -1:
        return cache[row][col] 

    if (row==n-1 and col==n-1):
        return 1

    

    bool1 = jump(row+arr[row][col], col, n)
    bool2 = jump(row, col+arr[row][col], n)

    if (bool1==1 or bool2==1):
        cache[row][col] = 1
        return cache[row][col]
    else:
        cache[row][col] = 0
        return cache[row][col]



arr=[]
cache=[]
c = int(input())
for i in range(c):
    arr.clear()
    cache.clear()
    
    n=int(input())
    cache = [[-1]*n for _ in range(n)]
    for j in range(n):
        temp=list(map(int, input().split()))
        arr.append(temp)
    # print(arr)
    tmp = jump(0, 0, n)
    if tmp == 1:
        print("YES")
    else:
        print("NO")