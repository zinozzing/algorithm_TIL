# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

N = int(input())
cnt=0
for i in range(N-1, -1, -1):
    A,B = map(int, input().split())
    cnt= cnt+1
    # for j in range(1, cnt):
    #     j = j+1
    print("Case #{}: {} + {} = {}".format(cnt, A, B, A+B))