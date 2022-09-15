# 풀이 :
# (1) 연속된 단어가 같으면 pass
# (2) 연속된 단어가 그 이후에 있으면 cnt에서 빼주기 (indexing 이용)

N = int(input())
cnt = N

for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break

print(cnt)