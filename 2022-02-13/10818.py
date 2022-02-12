# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())
num = list(map(int, input().split()))

max = num[0]
min = num[0]

for i in range(1, N):
    if num[i] > max:
        max = num[i]
    elif num[i] < min:
        min = num[i]

print(min,max)