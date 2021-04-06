import math
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

minusCount = 0
plusCount = 0
minusArr = []
plusArr = []

for i in range(len(arr)):
    if arr[i] > 0:
        plusCount += 1
        plusArr.append(arr[i])
    else:
        minusCount += 1
        minusArr.append(-arr[i])


plusArr.sort()
minusArr.sort()
plusMany = len(plusArr)
minusMany = len(minusArr)


if (plusMany > 0 and minusMany > 0):
    distance1 = 0
    for i in range(plusMany//m):
        distance1 += plusArr[m*i + plusMany % m - 1]*2

    if (plusMany/m - plusMany//m != 0):
        distance1 += plusArr[m*(plusMany//m) + plusMany % m - 1]


    for i in range(minusMany//m):
        distance1 += minusArr[m*i + minusMany % m - 1]*2
    if (minusMany/m - minusMany//m != 0):
        distance1 += minusArr[m*(minusMany//m) + minusMany % m - 1] * 2


    distance2 = 0
    for i in range(plusMany//m):
        distance2 += plusArr[m*i + plusMany % m - 1]*2

    if (plusMany/m - plusMany//m != 0):
        distance2 += plusArr[m*(plusMany//m) + plusMany % m - 1] * 2


    for i in range(minusMany//m):
        distance2 += minusArr[m*i + minusMany % m - 1]*2
    if (minusMany/m - minusMany//m != 0):
        distance2 += minusArr[m*(minusMany//m) + minusMany % m - 1]
    print(min(distance1, distance2))

elif (plusMany>0):  #plus만 존재시
    distance1=0
    if (plusMany%m != 0):
        for i in range(plusMany//m):
            distance1 += plusArr[m*i + plusMany % m - 1]*2
        distance1 += plusArr[m*(plusMany//m) + plusMany % m - 1]
    else:
        for i in range(plusMany//m-1):
            distance1 += plusArr[m*(i+1)-1] * 2
        distance1 += plusArr[plusMany-1]

    print(distance1)


else:   #minus만 존재시
    distance1=0
    if (minusMany%m != 0):
        for i in range(minusMany//m):
            distance1 += minusArr[m*i + minusMany % m - 1]*2
        distance1 += minusArr[m*(minusMany//m) + minusMany % m - 1]
    else:
        for i in range(minusMany//m-1):
            distance1 += minusArr[m*(i+1) - 1]*2
        distance1 += minusArr[minusMany- 1]

    print(distance1)