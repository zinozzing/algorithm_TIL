N = int(input())
line = 1

while N > line :
    N = N - line
    line = line + 1

if line % 2 == 0 :
    num1 = N
    num2 = line - N + 1
elif line % 2 == 1 :
    num1 = line - N + 1
    num2 = N

print(num1,'/',num2,sep = "")