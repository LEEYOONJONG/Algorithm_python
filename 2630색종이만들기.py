def colorpaper(rowstart, rowend, colstart, colend, n):
    global blueCount
    global whiteCount
    # all check
    forcheck=arr[rowstart][colstart]
    allSame=True
    for row in range(rowstart, rowend+1):
        for col in range(colstart, colend+1):
            if (arr[row][col] != forcheck):
                allSame=False
                break
        if allSame==False:
            break
    
    if allSame==True:
        if forcheck == 1: #파랑
            blueCount += 1
            return
        else:
            whiteCount += 1
    
    else:
        colorpaper(rowstart, rowstart+n//2-1, colstart, colstart+n//2-1, n//2)
        colorpaper(rowstart, rowstart+n//2-1, colstart+n//2, colend, n//2)
        colorpaper(rowstart+n//2, rowend, colstart, colstart+n//2-1, n//2)
        colorpaper(rowstart+n//2, rowend, colstart+n//2, colend, n//2)

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

blueCount=0
whiteCount=0

colorpaper(0, n-1, 0, n-1, n)

print(whiteCount)
print(blueCount)

