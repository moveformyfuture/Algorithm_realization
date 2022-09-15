def is_self_num(n : int):
    num = n
    for i in list(str(n)):
        num += int(i)
    
    return num

res = []
array = [is_self_num(i) for i in range(1, 10001)]

for i in range(1, 10001):
    if i in array: pass
    else: print(i)