# sourSum=1
# bitterSum=0

resultList=[]

# count는 재료를 실제로 더한 횟수
def calc(index, sourSum, bitterSum, count):
    if (index==n):
        if (count != 0): # count가 0이면 재료를 아무것도 더하지 않은 경우이므로 제외
            resultList.append(max(sourSum, bitterSum) - min(sourSum, bitterSum))
        return
    calc(index+1, sourSum*a[index], bitterSum+b[index], count+1) # 재료를 더한 경우의 재귀
    calc(index+1, sourSum, bitterSum, count) # 재료를 더하지 않은 경우의 재귀


n = int(input())
a = []
b = []

for i in range(n):
    tmpa, tmpb = map(int, input().split())
    a.append(tmpa)
    b.append(tmpb)


calc(0, 1, 0, 0)
print(min(resultList))