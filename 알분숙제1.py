import random
import time

def exchangesort(data): 
    #(2) exchange sort 알고리즘 구현하기
    len_data = len(data)
    for i in range(len_data-1):
        for j in range(i+1, len_data):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

def mergesort(data): #(3) merge sort 알고리즘 구현하기
    def sort(low, high):
        if high-low < 2:
            return
        mid = (low+high)//2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
    
    def merge(low, mid, high):
        temp=[]
        l, h = low, mid

        while l<mid and h<high:
            if data[l] < data[h]:
                temp.append(data[l])
                l += 1
            else:
                temp.append(data[h])
                h+=1
        while l<mid:
            temp.append(data[l])
            l+=1
        while h<high:
            temp.append(data[h])
            h += 1
        for i in range(low, high):
            data[i] = temp[i-low]
    return sort(0, len(data))

n = int(input("n을 입력하세요 : "))

data=[]
for i in range(n): # (1) n개의 데이타를 random으로 생성한다
    tmp = random.randint(1, 100)
    data.append(tmp)
data2 = data.copy()

exchange_start = time.time()
exchangesort(data)
exchange_end = time.time()
print("exchange sort의 시간은 ", exchange_end-exchange_start)

merge_start = time.time()
mergesort(data2)
merge_end = time.time()
print("merge sort의 시간은 ", merge_end-merge_start)
