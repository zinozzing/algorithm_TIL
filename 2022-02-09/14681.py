# x,y 좌표를 입력받아 해당하는 사분면 찾기
x = int(input())
y = int(input())

if x>0 and y>0:
    print(1)
elif x<0 and y<0:
    print(3)
elif x<0 and y>0:
    print(2)
elif x>0 and y<0:
    print(4)
    