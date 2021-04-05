import sys
sys.setrecursionlimit(100010)

def oilbank(start, end):
    if start==end:
        return 0
    
    minIndex = -1
    minPrice = 1000000001
    for i in range(start, end): # 최소 index 구하기 위해
        if price[i] < minPrice:
            minIndex = i
            minPrice = price[i]
    
    costSum = 0
    for i in range(minIndex, end):
        costSum += minPrice*dist[i]
    
    return costSum + oilbank(start, minIndex)



n = int(input())


dist = list(map(int, input().split()))
# dist.append(0)
price = list(map(int, input().split()))

print(oilbank(0, n-1))