n = int(input())
arr = list(map(int, input().split()))
arr.sort()

sum=0

for i in range(n):
    
        if (sum + 2 <= arr[i]):
           
            break
        else:
            sum += arr[i]
print(sum+1)