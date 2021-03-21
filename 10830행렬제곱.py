def matrixMultiply(arr1, arr2):
    global n
    newArr=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            sum=0
            for k in range(n):
                sum += arr1[i][k]*arr2[k][j]
            newArr[i][j] = sum%1000
    return newArr

def matrix(degree):
    global arr

    if degree==1:
        return arr
    elif degree%2==1:
        return matrixMultiply(arr, matrix(degree-1))
    else:
        half = matrix(degree/2)
        return matrixMultiply(half, half)



n, b = map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))


calcArr= matrix(b)
for i in range(n):
    for j in range(n):
        print(calcArr[i][j]%1000, end=" ")
    print()