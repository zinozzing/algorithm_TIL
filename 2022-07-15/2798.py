# 블랙잭
# from itertools import combinations

# N, M = map(int, input().split())
# nums = list(map(int, input().split()))
# answer = []
# for combination in combinations(nums, 3):
#     x = int(combination[0]) 
#     y = int(combination[1])
#     z = int(combination[2])
#     answer.append(x+y+z)
# answer = set(answer)
# answer = list(answer)
# answer.sort()

# min_num = 0
# for i in answer:
#     if abs(M-i) <= abs(M-min_num):
#         min_num = i
# print(min_num)


import itertools

N, M = map(int, input().split())
card_num = list(map(int, input().split()))


combi_sum = [sum(combi) for combi in itertools.combinations(card_num, 3) if sum(combi) <= M]

print(max(combi_sum))



