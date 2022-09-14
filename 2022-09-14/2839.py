# 설탕 배달
N = int(input())
plasticBag = 0

while True:
    if N%5 == 0:
        plasticBag += N//5
        break
    else:
        N -= 3
        plasticBag += 1
        if N < 0:
            plasticBag = -1
            break

print(plasticBag)