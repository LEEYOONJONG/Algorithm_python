import sys
sys.setrecursionlimit(10**8)

arr=[]
def fib(n):
    if (arr[n] != -1):
        return arr[n]
    
    arr[n] = (fib(n-1) + fib(n-2)) % 1000000000
    return arr[n]


n=int(input())
if n>0:
    print(1)
elif n==0:
    print(0)
else:
    print(-1)
arr=[-1]*1000001
arr[0]=0
arr[1]=1

tmp = abs(n)
print(fib(tmp))


