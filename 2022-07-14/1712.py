# 손익분기점

fixed, non_fixed, price = map(int, input().split())

if non_fixed >= price:
    print(-1)
else:
    print(fixed//(price-non_fixed)+1)



