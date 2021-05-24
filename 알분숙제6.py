# import utility
import sys

########################
# 문제 1

def printMatrix(d):
    m = len(d) 
    n = len(d[0])
    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j],end=" ")
        print()



e = {0: [1, 2, 3], 1: [2, 5], 2: [3, 4, 5, 6], 3: [4, 6], 4: [6, 7]} 
n = 8
a = [[0 for j in range(0, n)] for i in range(0, n)] 
for i in range(0, n-1):
    for j in range(i+1, n):
        if i in e:
            if j in e[i]:
                a[i][j] = 1 
                a[j][i] = 1

printMatrix(a)

visited = n*[0]
global count
count = 1

# 깊이우선검색 구현
def DFS(a, v):
    global count
    print(count, v)
    visited[v] = 1
    count += 1
    if (v not in e):
        return
    for i in range(len(e[v])):
        toIndex = e[v][i]
        if (visited[toIndex] == 0):
            visited[toIndex] = 1
            DFS(a, toIndex)
print("1번 문제")
DFS(a, 0)
print()
#################################
#  문제 2

global count2
count2=0

def promising(i, col):
    k=0
    switch = True
    while(k<i and switch == True):
        if (col[i] == col[k] or abs(col[i]-col[k]) == i-k) :
            switch = False
        k += 1
    return switch

def queens(n, i, col):
    global count2

    if (promising(i, col)):
        if (i==n-1):
            count2 += 1
            if (count2 == 3): # 3번째 해라면 출력한다.
                for j in range(n):
                    print(col[j], end=" ")
                print()
        else:
            for j in range(n):
                col[i+1] = j
                queens(n, i+1, col)

n=7
col = n*[0]
print("2번 문제")

queens(n, 0, col)
print("해의 총 개수는 ", count2, "개 입니다.")