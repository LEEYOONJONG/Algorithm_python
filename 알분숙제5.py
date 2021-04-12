
########################################
## 1번 과제
## 
print("1번 과제")
print()
def print_inOrder(root):
    if not root:
        return 
    print_inOrder(root.l_child)
    print(root.data) 
    print_inOrder(root.r_child)

def print_preOrder(root): 
    if not root:
        return
    print(root.data) 
    print_preOrder(root.l_child) 
    print_preOrder(root.r_child)

def print_postOrder(root): 
    if not root:
        return
    print_postOrder(root.l_child)
    print_postOrder(root.r_child) 
    print(root.data)

def printMatrix(d):
    m = len(d) 
    n = len(d[0])
    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j],end=" ")
        print()

def printMatrixF(d):
    n = len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print("%5.2f" % d[i][j],end=" ")
        print()

class Node:
    def __init__(self, data):
        self.l_child = None 
        self.r_child = None
        self.data = data

def tree(key, r, i, j): 
    k = r[i][j]
    if(k == 0):
        return
    else:
        p = Node(key[k])
        p.l_child = tree(key, r, i, k-1) 
        p.r_child = tree(key, r, k+1, j) 
        return p

key = [" ", "A", "B", "C", "D", "E"] 
p = [0, 4/15, 5/15, 1/15, 3/15, 2/15] 
n = len(p)-1

a = [[0 for j in range(0, n+2)] for i in range(0, n+2)] # 검색시간 최적값
r = [[0 for j in range(0, n+2)] for i in range(0, n+2)] # 그때의 root 값

for i in range(1, n+1):
    a[i][i-1] = 0
    a[i][i] = p[i] 
    r[i][i] = i 
    r[i][i-1] = 0
a[n+1][n] = 0 
r[n+1][n] = 0

# 구현
for diagonal in range(1, n):
    for i in range(1, n-diagonal+1):
        j = i+diagonal
        minimum=10000
        savedK=-1
        for k in range(i, j+1):
            tmp = a[i][k-1]+a[k+1][j]
            if tmp<minimum:
                minimum = tmp
                savedK = k
        psum=0
        for k in range(i, j+1):
            psum += p[k]
        a[i][j] = minimum + psum
        r[i][j] = savedK

#

printMatrixF(a) 
print() 
printMatrix(r)

root = tree(key, r, 1, n) 
print_inOrder(root) 
print() 
print_preOrder(root)





###############################################################
## 2번 과제
##
print()
print("2번 과제")
print()

a = ['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C', 'C'] 
b = ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A']
m = len(a)
n = len(b)
table = [[0 for j in range(0, n+1)] for i in range(0, m+1)]
minindex = [[(0, 0) for j in range(0, n+1)] for i in range(0, m+1)]
for j in range(n-1, -1, -1):
    table[m][j] = table[m][j+1]+2
for i in range(m-1, -1, -1):
    table[i][n] = table[i+1][n]+2

# 테이블 생성 구현
def opt(i, j):
    global m, n
    if i==m:
        table[i][j] = 2*(n-j)
        
    elif j==n:
        table[i][j] = 2*(m-i)
    else:
        if a[i] == b[j]:
            penalty = 0
        else:
            penalty = 1

        opt1 = opt(i+1, j+1)+penalty
        opt2 = opt(i+1, j)+2
        opt3 = opt(i, j+1)+2
        table[i][j] = min(opt1, opt2, opt3)

        if table[i][j] == opt1:
            minindex[i][j] = (i+1, j+1)
        elif table[i][j] == opt2:
            minindex[i][j] = (i+1, j)
        else:
            minindex[i][j] = (i, j+1)

        
    return table[i][j]

####

opt(0,0)
printMatrix(table) 
x = 0
y = 0

while (x < m and y < n):
    tx, ty = x, y
    print(minindex[x][y])
    (x, y) = minindex[x][y]
    if x == tx + 1 and y == ty+1:
        print(a[tx], " ", b[ty]) 
    elif x == tx and y == ty+1: # x는 틈
        print(" - ", " ", b[ty]) 
    else:                       # y는 틈
        print(a[tx], " ", " -")
