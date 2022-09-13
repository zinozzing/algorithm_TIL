# 덩치
N = int(input())
spec = []
win = []
for i in range(N):
    x, y = map(int, input().split())
    spec.append((x,y))

for j in range(N):
    point = 0
    for k in range(N):
        if (spec[j][0] >= spec[k][0]) or (spec[j][1] >= spec[k][1]):
            point = point+1
    win.append(point)

for l in range(N):
    print(N-win[l]+1, end=" ")