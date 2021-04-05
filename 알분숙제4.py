import copy

def path(p, q, r): # p, 5, 3
    if (p[q-1][r-1] != 0):
        path(p, q, p[q-1][r-1])
        print(f"v{p[q-1][r-1]}", end=" ")
        path(p, p[q-1][r-1], r)

def allShortestPath(g, n):
# d는 최단거리의 길이가 포함된 배열(결과)
# 
    d = copy.deepcopy(g)
    p=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if (d[i][j] > d[i][k]+d[k][j]):
                    d[i][j] = d[i][k]+d[k][j]
                    p[i][j] = k+1

    return d, p

def printMatrix(d):
    n = len(d[0])
    for i in range(0, n):
        for j in range(0, n):
            print(d[i][j], end=" ")
        print()


inf = 1000
g = [[0,1,inf,1,5],
[9,0,3,2,inf],
[inf,inf,0,4,inf],
[inf,inf,2,0,3],
[3,inf,inf,inf,0]]

printMatrix(g)
d, p = allShortestPath(g, 5)
print()
printMatrix(d)
print()
printMatrix(p)

path(p, 5, 3) # 5 to 3
print()