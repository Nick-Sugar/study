
for i in range(2,101):
    half = i//2 
    flag = True
    for n in range(2,half):
        if i % n == 0:
            flag = False
            break
    if flag:
        print(i,end=",")