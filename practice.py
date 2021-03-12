from itertools import combinations

colList=[]
for i in range(4): # [0,1,2,3,4]
    colList.append(i)


aa = list(combinations(colList, 2))
print(aa)
print(aa[3][1])
