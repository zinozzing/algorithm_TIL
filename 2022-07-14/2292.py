n = int(input())

pileup = 1 # 1부터 시작
cnt = 1

while n > pileup:
    pileup += 6 * cnt
    cnt += 1
    
print(cnt)