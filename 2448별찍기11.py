# 시간초과
import sys

n = int(input())
center = n-1

def star(i, j, n): # n = 12
    if i<3:
        if (i==0 and j==center):
            print("*",end="")
        elif (i==1 and (j==center-1 or j==center+1)):
            print("*",end="")
        elif (i==2 and (center-2<=j and j<=center+2)):
            print("*",end="")
        else:
            print(" ",end="")

    elif i >= n/2:
        if j<center:
            star(i-n/2, j+n/2, n/2)
        elif j>center:
            star(i-n/2, j-n/2, n/2)
        else:
            print(" ",end="")

    else:
        star(i, j, n/2)







for i in range(n):
    for j in range((n//3)*6 - 1):
        star(i, j, n)
    print()