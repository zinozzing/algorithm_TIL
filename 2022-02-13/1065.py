# 한수 : 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 


N = int(input())

def find_hansu(N):
    cnt = 0
    for j in range(1, N+1):
        num_set= set()
        ch_N = str(j)
        for i in range(len(ch_N)-1):
            num_set.add(int(ch_N[i+1])-int(ch_N[i])) 
        if len(num_set) == 1 or len(num_set) == 0:
            cnt = cnt+1 
    return cnt

print(find_hansu(N))