# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

constant_num = input().split(" ")

first_reverse = constant_num[0][::-1]
second_reverse = constant_num[1][::-1]

print(max(int(first_reverse), int(second_reverse)))