
def quadtree(rowstart, rowend, colstart, colend): # 0,7,0,7
    # 우선 전부 같은지 확인
    check = mylist[rowstart][colstart]
    allSame = True
    for i in range(rowstart, rowend+1):
        for j in range(colstart, colend+1):
            if (check != mylist[i][j]):
                allSame = False
                break
        if allSame == False:
            break
    
    if allSame == True:
        print(check, end='')
        return
    else:
        print("(", end='')
        quadtree(rowstart,(rowstart+rowend)//2, colstart, (colstart+colend)//2) #첫번째사분면
        quadtree(rowstart,(rowstart+rowend)//2, (colstart+colend)//2+1, colend) #첫번째사분면
        quadtree((rowstart+rowend)//2+1,rowend, colstart, (colstart+colend)//2) #첫번째사분면
        quadtree((rowstart+rowend)//2+1,rowend, (colstart+colend)//2+1, colend) #첫번째사분면
        


        print(")", end='')
    

n = int(input())
mylist=[]
for i in range(n):
    mylist.append(list(input()))
quadtree(0,n-1,0,n-1)
