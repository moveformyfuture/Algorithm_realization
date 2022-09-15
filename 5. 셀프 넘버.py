def is_self_num(n : int): # 생성자 만드는 함수를 정의
    num = n
    for i in list(str(n)): # list에 str 넣으면 숫자가 쪼개짐
        num += int(i)
    
    return num

res = []
array = [is_self_num(i) for i in range(1, 10001)] 

# 생성자가 아닌 것만 print
for i in range(1, 10001):
    if i in array: pass
    else: print(i)