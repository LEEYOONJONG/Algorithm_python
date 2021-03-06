import numpy as np

origin = np.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,2,2,2,2,2,1,1,1,0],
    [0,2,2,2,2,2,1,1,1,0],
    [0,2,2,2,2,2,1,1,1,0],
    [0,2,2,2,2,2,1,1,1,0],
    [0,2,2,2,9,9,9,9,9,0],
    [0,2,2,2,9,9,9,9,9,0],
    [0,2,2,2,9,9,9,9,9,0],
    [0,2,2,2,9,9,9,9,9,0],
    [0,0,0,0,0,0,0,0,0,0]
])
weight = np.array([
    [-1,-1,-1],
    [0,0,0],
    [1,1,1]
])
for i in range(1, 9):
    print("[",end="")
    for j in range(1, 9):
        sum = origin[i-1][j-1]*weight[0][0] + origin[i-1][j]*weight[0][1] + origin[i-1][j+1]*weight[0][2] + origin[i][j-1]*weight[1][0] + origin[i][j]*weight[1][1] + origin[i][j+1]*weight[1][2] + origin[i+1][j-1]*weight[2][0] + origin[i+1][j]*weight[2][1] + origin[i+1][j+1]*weight[2][2] + 0.5
        print(sum, end=", ")
    print("],")

origin2 = np.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0, 4.5, 6.5, 6.5, 6.5, 5.5, 4.5, 3.5, 2.5, 0],
    [0,0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,0 ],
    [0,0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,0],
    [0,0.5, 0.5, 7.5, 14.5, 22.5, 23.5, 24.5, 16.5,0 ],
    [0,0.5, 0.5, 7.5, 14.5, 22.5, 23.5, 24.5, 16.5,0 ],
    [0,0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,0],
    [0,0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,0 ],
    [0,-3.5, -5.5, -12.5, -19.5, -26.5, -26.5, -26.5, -17.5,0 ],
    [0,0,0,0,0,0,0,0,0,0]
])

for i in range(1, 9):
    for j in range(1, 9):
        print(max(origin2[i-1][j-1] , origin2[i-1][j] , origin2[i-1][j+1] , origin2[i][j-1] , origin2[i][j], origin2[i][j+1] , origin2[i+1][j-1] , origin2[i+1][j], origin2[i+1][j+1]), end=" ")
    print()