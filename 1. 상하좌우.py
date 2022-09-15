# 풀이
# (1) L, R, U, D를 입력받고, 그에 매칭하게 이동하도록 좌표 구성
# (2) for문을 활용해 이동 구현
# (3) 예외처리 : 공간을 벗어나는 경우 

# 데이터 입력
n = int(input())
move = input().split()
x, y = 1, 1

# 좌표 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 하나씩 확인
for plan in move : 
    # 이동 후 좌표 구하기
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 공간을 벗어나는 경우 무시
    if (nx < 1 or ny < 1 or nx > n or ny > n) :
        continue
    
    x, y = nx, ny

print(x, y)