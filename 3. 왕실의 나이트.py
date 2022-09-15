# 풀이
# (1) 입력받은 데이터의 행과 열을 구분함
# (2) 갈 수 있는 step을 정의
# (3) for문을 활용해 이동 가능한지 확인
# (4) 좌표계 밖으로 나가는지 확인(예외처리 :or, 확인 : and)


input_data = input() # str형으로 입력받음

# 행과 열 구분
row = int(input_data[1]) 
column = ord(intput_data[0]) - ord('a') + 1 # 원하는 좌표계로 오도록 맞춰주는 수식

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0

# 이동 가능한지 확인
for step in steps : 
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    
    # 좌표계 밖으로 나가는지 확인 (cnt 증가)
    if next_row >=1 and next_column >= 1 and next_row <=8 and next_column <=8 :
        result += 1

print(result)