# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

C = int(input())
for _ in range(C):
    N = list(map(float, input().split()))
    avg = (sum(N)-N[0])/N[0]
    cnt = 0
    for i in N[1:]:
        if i > avg:
            cnt += 1
    result = cnt/(len(N)-1)*100
    print(f'{result:.3f}%')
