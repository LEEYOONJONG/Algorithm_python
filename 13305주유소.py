import sys
sys.setrecursionlimit(100010)

def oilbank(start, end): ## 시간초과 나는 코드
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

def oilbank2(start, end):
    minPrice = 1000000001

    res = 0
    
    for i in range(start, end):
        if minPrice > price[i]:
            minPrice = price[i]
            res += minPrice*dist[i]
        else:
            res += minPrice*dist[i]

    return res

n = int(input())


dist = list(map(int, input().split()))
price = list(map(int, input().split()))

print(oilbank2(0, n-1))