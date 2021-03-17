n=int(input())
arr=[]
for i in range(n):
    temp=list(map(int, input().split()))
    arr.append(temp)

def move(k, arr):
    global n
    if (k==1): #위로
        for col in range(n):
            for row in range(n):
                # 끌어당기기
                
                if arr[row][col] == arr[row+1][col]:
                    arr[row][col] += arr[row+1][col]
                    arr[row+1][col] = 0
                

