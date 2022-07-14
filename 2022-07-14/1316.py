# 그룹단어체커

cnt = 0
n = int(input())

for i in range(n):
    word = input()
    word_li = list(word)
    checked_li = []
    error = False
    for j in range(len(word_li)):
        if word_li[j] in checked_li:
            if word_li[j] == word_li[j-1]:
                continue
            error = True
            break
        else:
            checked_li.append(word_li[j])
    if not error:
        cnt += 1
print(cnt)