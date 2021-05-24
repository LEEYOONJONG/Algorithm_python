import sys

############# 1번
print("1번")
def promising(i,weight, total):
    global W, n
    return (weight+total >= W) and (weight == W or weight+w[i+1] <= W)

def s_s(i, weight, total, include):
    global W, n
    if (promising(i, weight, total)):
        if (weight == W):
            print("sol ", include)
        else:
            include[i+1] = 1
            s_s(i+1, weight+w[i+1], total-w[i+1], include)
            include[i+1] = 0
            s_s(i+1, weight, total-w[i+1], include)

n = 6
w = [1,2,3,4,5,6]
w.sort()
W = 9
print("items =",w, "W =", W)
include = n*[0]
total = 0
for k in w:
    total+=k
s_s(-1, 0, total, include)



############ 2번
print("2번")
def color(i, vcolor):
    global m2, n2
    if (promising2(i, vcolor)):
        if (i==n2-1):
            print(vcolor)
        else:
            for idx in range(1, m2+1):
                vcolor[i+1] = idx
                color(i+1, vcolor)

def promising2(i, vcolor):
    switch = True
    j=0
    while(j<i and switch):
        if (W2[i][j]==1 and vcolor[i]==vcolor[j]):
            switch = False
        j+=1
    return switch
  
n2 = 4
W2 = [[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]] 
vcolor = n2*[0]
m2 = 3
color(-1,vcolor)