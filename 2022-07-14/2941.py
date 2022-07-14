# 크로아티아 알파벳

croa_li = ['c=','c-','dz=','d-','lj','nj','s=','z=']

str = input()

for i in croa_li:
    str = str.replace(i, '*')

print(len(str))