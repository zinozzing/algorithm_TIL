# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
num = list(int(input()) for _ in range(3))
gop = num[0] * num[1] * num[2]
cnt = str(gop)
for i in range(10):
    print(cnt.count(str(i)))
