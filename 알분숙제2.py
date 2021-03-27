
def mergeSort(n, S):
    global mergesortSpace
    middle = n//2
    U=[]
    V=[]
    if (n>1):
        U=S[0:middle]
        V=S[middle:n]
        mergesortSpace += 2 # 추가 저장공간 2개씩 필요
        mergeSort(middle, U)
        mergeSort(n-middle, V)
        merge(middle, n-middle, U, V, S)



def merge(h,m,U,V,S): # middle, n-middle, ...
    i,j,k= 0, 0, 0
    while(i<h and j<m):
        if (U[i] < V[j]):
            S[k]=U[i]
            i += 1
        else :
            S[k]=V[j]
            j += 1
        k += 1
    
    if i>=h:
        while(j<m):
            S[k] = V[j]
            j+=1
            k+=1
    else:
        while(i<h):
            S[k]=U[i]
            i+=1
            k+=1
    



def mergeSort2(s, low, high): 
    if low<high:
        mid = (low+high)//2
        mergeSort2(s, low, mid)
        mergeSort2(s, mid+1, high)
        merge2(s, low, mid, high)

def merge2(s, low, mid, high):
    global mergesort2Space
    i, j, k = low, mid+1, low
    u=[0 for _ in range(high+1)]
    while(i<=mid and j<=high):
        if s[i]<s[j]:
            u[k]=s[i]
            i += 1
        else:
            u[k]=s[j]
            j += 1
        k += 1

    if (i>mid):
        while(j<=high):
            u[k]=s[j]
            j+=1
            k+=1
    else:
        while(i<=mid):
            u[k]=s[i]
            i+=1
            k+=1


    if mergesort2Space < high-low+1: # 병합하기 위한 배열의 크기(high-low+1)의 최댓값을 구한다.
        mergesort2Space = high-low+1
    
    s[low:high+1] = u[low:high+1] # u 반납


mergesortSpace = 0
mergesort2Space = 0

s=[3,16,13,1 ,9,2,7,5, 8,4,11,6, 15,14,10,12]
s2=s[:]
print("mergeSort 적용 전 : ", s)
mergeSort(16, s)
print("mergeSort 적용 후 : ", s)
print("mergeSort에 필요한 추가적인 저장공간의 개수 : ", mergesortSpace)

print("mergeSort2 적용 전 : ", s2)
mergeSort2(s2, 0, 15)
print("mergeSort2 적용 후 : ", s2)
print("mergeSort2에 필요한 추가적인 저장공간의 개수 : ", mergesort2Space)