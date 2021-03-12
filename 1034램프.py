from itertools import combinations

maximum=0
def lamp(r): # 5C2
    global m # 전역변수 m을 사용하겠다. 5
    global mylist
    global maximum
    colList=[]
    for i in range(m): # [0,1,2,3,4]
        colList.append(i)
    
    orderList = list(combinations(colList, r)) # [(0,1),(0,2), ...]

    for i in range(len(orderList)):
        copiedList = mylist.copy()
        for j in range(r):  # (1, 2)
            # copiedArr의 orderList[i][j]열 뒤집기
            # turn(copiedArr, orderList[i][j]) # 
            for k in range(len(mylist)): # 행
                if copiedList[k][orderList[i][j]] == '0':
                    copiedList[k][orderList[i][j]] = '1'
                else:
                    copiedList[k][orderList[i][j]] ='0'
        # 켜져 있는 행 체크
        count=0
        for j in range(len(copiedList)):
            isOn = True
            for k in range(m-1):
                if not(copiedList[j][k]=='1' and copiedList[j][k+1]=='1'):
                    isOn = False
                    break
            if isOn == True:
                count += 1
        
        if count > maximum:
            maximum = count



n, m = map(int, input().split())
mylist=[]
for i in range(n):
    mylist.append(list(input()))

k = int(input())

for i in range(k, -1, -2):
    lamp(i) # mCi

print(maximum)