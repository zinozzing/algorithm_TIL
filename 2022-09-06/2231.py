# 분해합
N = int(input())
min_target = abs(N - (len(str(N)) * 9))

def sum_digit(n):
    num_li = []
    len_num = len(str(n))
    for i in range(len_num-1, -1, -1):
        num_li.append(n//(10**i)%10)
    return sum(num_li)

for j in range(N):
    num = sum_digit(j)
    if j+num == N:
        print(j)
        break
    if j == N-1:
        print(0)