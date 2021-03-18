import copy


def run(arr, cnt):
    global max
    global n
    if cnt>=5: # 최대 횟수인 5을 다채웠다면
        # max보다 큰 원소가 있다면 max 업데이트
        for row in range(n):
            for col in range(n):
                if (arr[row][col] > max):
                    max = arr[row][col]
        return
    for i in range(5):
        run(move(i, arr), cnt+1)



def move(k, paramArr): # paramArr를 직접 바꾸지 않음!
    arr = copy.deepcopy(paramArr)
    global n
    if (k==1): #위로
        for col in range(n):
            # 중간에 0은 아래로 보내고 시작하자.
            rowIndex=0 
            for row in range(n):
                if (arr[row][col] != 0):
                    arr[rowIndex][col] = arr[row][col]
                    rowIndex+=1
            #나머지는 0으로.
            for row in range(rowIndex, n):
                arr[row][col] = 0

            # 더하는 작업
            for row in range(n-1):
                if (arr[row][col] == arr[row+1][col]):
                    arr[row][col] += arr[row+1][col]
                    arr[row+1][col] = 0

            # 다시 중간에 0은 아래로 보내고 시작하자.
            rowIndex=0 
            for row in range(n):
                if (arr[row][col] != 0):
                    arr[rowIndex][col] = arr[row][col]
                    rowIndex+=1
            #나머지는 0으로.
            for row in range(rowIndex, n):
                arr[row][col] = 0
    elif (k==2): #왼쪽으로
        for row in range(n):
            # 중간에 0은 오른쪽로 보내고 시작하자.
            colIndex=0 
            for col in range(n):
                if (arr[row][col] != 0):
                    arr[row][colIndex] = arr[row][col]
                    colIndex+=1
            #나머지는 0으로.
            for col in range(colIndex, n):
                arr[row][col] = 0
                
            # 더하는 작업
            for col in range(n-1):
                if (arr[row][col] == arr[row][col+1]):
                    arr[row][col] += arr[row][col+1]
                    arr[row][col+1] = 0

            # 중간에 0은 오른쪽으로 보내고 시작하자.
            colIndex=0 
            for col in range(n):
                if (arr[row][col] != 0):
                    arr[row][colIndex] = arr[row][col]
                    colIndex+=1
            #나머지는 0으로.
            for col in range(colIndex, n):
                arr[row][col] = 0
    elif (k==3): # 오른쪽으로
        for row in range(n):
            # 중간에 0은 왼쪽으로 보내자
            colIndex=n-1
            for col in range(n-1, -1, -1): #오른쪽에서 왼쪽으로 접근해가며
                if (arr[row][col] != 0):
                    arr[row][colIndex] = arr[row][col]
                    colIndex -= 1
            # 나머지는 0으로.
            for col in range(colIndex, -1, -1):
                arr[row][col] = 0
            # 더하기
            for col in range(n-1, 0, -1):
                if (arr[row][col] == arr[row][col-1]):
                    arr[row][col] += arr[row][col-1]
                    arr[row][col-1] = 0
            # 다시 중간에 0은 왼쪽으로 보내자
            colIndex=n-1
            for col in range(n-1, -1, -1): #오른쪽에서 왼쪽으로 접근해가며
                if (arr[row][col] != 0):
                    arr[row][colIndex] = arr[row][col]
                    colIndex -= 1
            # 나머지는 0으로.
            for col in range(colIndex, -1, -1):
                arr[row][col] = 0
    elif (k==4): #아래로
        for col in range(n):
            # 중간에 0 은 위로 보내고 시작
            rowIndex = n-1
            for row in range(n-1, -1, -1):
                if (arr[row][col] != 0):
                    arr[rowIndex][col] = arr[row][col]
                    rowIndex -= 1
            #나머지는 0
            for row in range(rowIndex, -1, -1):
                arr[row][col] =0
            
            #더하는 작업
            for row in range(n-1, 0, -1):
                if (arr[row][col] == arr[row-1][col]):
                    arr[row][col] += arr[row-1][col]
                    arr[row-1][col] = 0
            # 다시 중간에 0 은 위로 보내고 시작
            rowIndex = n-1
            for row in range(n-1, -1, -1):
                if (arr[row][col] != 0):
                    arr[rowIndex][col] = arr[row][col]
                    rowIndex -= 1
            #나머지는 0
            for row in range(rowIndex, -1, -1):
                arr[row][col] =0
    return arr


n=int(input())
arr=[]
for i in range(n):
    temp=list(map(int, input().split()))
    arr.append(temp)
max=-1
run(arr, 0)
print(max)


