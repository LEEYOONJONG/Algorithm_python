# 문자열 a의 첫문자를 pivot으로.
# 문자열 b의 맨 앞부터 a를 하나씩 대보며 가장 많이 겹칠때를 선정

a, b = input().split()

lengthA = len(a)
lengthB = len(b)
maxcount = 0

for i in range(lengthB-lengthA+1): # b 문자열의 시작점 지정
    count=0
    for j in range(lengthA): # a를 앞에서부터 하나씩 대보기
        if (a[j] == b[j+i]):
            count += 1
    if count > maxcount:
        maxcount = count

print(lengthA - maxcount)