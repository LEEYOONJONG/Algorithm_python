## r행 c열엔 어떤 수인가?
def z(rowstart, rowend, colstart, colend, num, order): # num은 덩어리의 변 #num=2,order=4
    global r
    global c
    if num==1:
        if rowstart==r and colstart==c:
            print(order)
            return
        else:
            return
    if (rowstart<=r and r<=rowstart+(num//2)-1 and colstart<=c and c<=colstart+(num//2)-1):
        z(rowstart, rowstart+(num//2)-1, colstart, colstart+(num//2)-1, num//2, order)
    elif (rowstart<=r and r<=rowstart+(num//2)-1 and colstart+num//2<=c and c<=colend):
        z(rowstart, rowstart+(num//2)-1, colstart+num//2, colend, num//2, order+(num//2)**2)
    elif (rowstart+num//2<=r and r<=rowend and colstart<=c and c<=colstart+(num//2)-1):
        z(rowstart+num//2, rowend, colstart, colstart+(num//2)-1, num//2, order+((num//2)**2)*2)
    else:
        z(rowstart+num//2, rowend, colstart+num//2, colend, num//2, order+((num//2)**2)*3) 


n, r, c = map(int, input().split())

num = 2 ** n # n=2 -> num = 2^2= 4
z(0, num-1, 0, num-1, num, 0)
