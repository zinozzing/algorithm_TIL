n = int(input())

pileup = 1 # 1λΆν° μμ
cnt = 1

while n > pileup:
    pileup += 6 * cnt
    cnt += 1
    
print(cnt)