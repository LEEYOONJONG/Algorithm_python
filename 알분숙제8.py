import queue
from queue import PriorityQueue 
def knapsack(i, profit, weight):
    global bestset
    global maxp

    if (weight <= W and profit > maxp):
        maxp = profit
        bestset = include[:]

    if (promising(i, weight, profit)):
        include[i+1] = 1
        knapsack(i+1, profit+p[i+1], weight+w[i+1])
        include[i+1] = 0
        knapsack(i+1, profit, weight)


def promising(i, weight, profit):
    global maxp, n
    if weight >= W:
        return False
    else:
        j = i+1 # 가능?
        bound = profit
        totweight = weight
        while(j < n and totweight+ w[j] <= W):
            totweight = totweight +w[j]
            bound = bound+p[j]
            j += 1
        k=j
        if k<n:
            bound = bound + (W-totweight)*p[k]/w[k]
        
        return bound > maxp


n=4
W=8
p=[48,55,16,16]
w=[4,5,4,8]
maxp=0
include=[0,0,0,0]
bestset=[0,0,0,0]
knapsack(-1, 0,0)
print("1번--")
print(maxp)
print(bestset)


class Node:
    def __init__(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit 
        self.bound = bound 
        self.include = include 
    def __lt__(self, other):
        return self.bound < other.bound
    

def kp_BestFS():
    global maxp2
    global bestset2
    q = PriorityQueue()
    temp = n*[0]
    v = Node(-1,0,0,0.0, temp)
    
    maxp2 = 0
    v.bound = compBound(v)
    
    q.put(v)

    while(q.empty()== False):
        v = q.get()
        # print("v.bound : ", v.bound)
        if (v.bound < maxp2):
            u = v
            u.level = v.level+1
            u.include = v.include[:]
            u.weight = v.weight + w[u.level]
            u.profit = v.profit + p[u.level]
            u.include[u.level] = 1
            u.bound = compBound(u)
            if (u.weight<=W and u.profit > maxp2):
                maxp2 = -u.profit
                bestset2 = u.include[:]
            # u.bound = compBound(u)
            if (u.bound < maxp2):
                # temp[u.level]=1
                # u.include = temp[:]
                q.put(u)
            u = v
            u.level = v.level+1
            u.include = v.include[:]
            u.profit = v.profit
            u.weight = v.weight
            u.bound = compBound(u)
            if (u.bound < maxp2):
                # temp[u.level]=0
                # u.include = temp[:]
                q.put(u)
        
    # bestset2 = temp[:]


def compBound(u):
    if u.weight >= W:
        return 0
    else:
        j = u.level+1
        res = u.profit
        totweight = u.weight
        while j<n and totweight + w[j] <= W:
            totweight = totweight + w[j]
            res = res + p[j]
            j+= 1
        k=j
        if (k<n):
            res = res+(W-totweight)*p[k]/w[k]
        return -res

include2 = n*[0]
maxp2 = 0
bestset2 = n*[0]
kp_BestFS()
print("2번--")
print(bestset2)
print(maxp2)
