'''
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
'''

N = int(input())
for i in range(N):
    cnt = 0
    li = []
    OX = str(input())
    for j in range(len(OX)):
        if OX[j] == 'O':
            cnt = cnt+1
            li.append(cnt)
        else:
            cnt = 0
    print(sum(li))