# 다이얼
word = input()
num_dict = {'1':[], '2':['A','B','C'], '3':['D','E','F'], '4':['G','H','I'], '5':['J','K','L'], '6':['M','N','O'], '7':['P','Q','R','S'], '8':['T','U','V'], '9':['W','X','Y','Z'], '0':[]}

num_li = [] 
for alpha in word:
    for i in range(len(num_dict)):
        if (alpha in num_dict[str(i)]):
            num_li.append(i)
            break

new_li = map(lambda x: x+1, num_li)
result = sum(new_li)
print(result)
            