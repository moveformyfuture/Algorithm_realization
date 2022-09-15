# 풀이 : '문자'가 포함되어 있는지 확인
# (1) 시간, 분, 초를 for문으로 구현
# (2) 3이 (str(i) + str(j) + str(k))에 있는지 확인


h = int(input())
cnt = 0

for i in range(h+1) :
    for j in range(60) : 
        for k in range(60) :
            if '3' in (str(i) + str(j) + str(k)) : # '3'이 () 에 있는지 확인
                cnt += 1
                
print(cnt)