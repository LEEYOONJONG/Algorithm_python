
def grape(start, count): # 인덱스 start의 원소를 포함시킨다.
    global n
    global arr
    global dp

    if start>=n: # base case
        return 0
    # if dp[start][count]!=-1:
    #     return dp[start][count]
    res = 0 
    if count==0:
        for i in range(start+1, start+3):
                    # 인덱스 i의 원소를 '포함 안시킬때'와 '포함시킬때'를 비교한다.
                    # '포함시킬때'는 i가 무엇이냐에 따라 앞으로 진입하는 grape의 count가 달라진다.  
            temp = max(arr[start], arr[start]+grape(i, (start+2) - i))

            # for문에서 각각 구한 temp 값중 가장 큰 값이 result가 된다.
            if (res < temp):
                res = temp

    elif count==1:
        for i in range(start+2, start+4):
            # 이 경우, 이전 포도잔에 한칸을 띄운 후 시작하므로 '포함시킬때'에도 count는 0으로 고정된다. 
            temp = max(arr[start], arr[start]+grape(i, 0))
            if (res < temp): 
                res = temp
    # print("dp[",start,"][",count,"] = ", res)
    dp[start][count] = res
    print("dp[",start,"][",count,"] = ", dp[start][count])
    
    return dp[start][count]

n = int(input())
arr = []
dp=[[-1]*2]*(n+10)

for i in range(n):
    arr.append(int(input()))
# print(arr)

maximum=0
for i in range(n):
    tmp = grape(i, 0)
    print(dp)
    if (maximum <tmp):
        print("-->", i," 일 때!",tmp)
        maximum = tmp

print(maximum)
