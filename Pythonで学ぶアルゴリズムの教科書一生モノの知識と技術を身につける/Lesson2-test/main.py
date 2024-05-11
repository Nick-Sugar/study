
# 2-1

a = [10,-5,0,19,6,2,77,8]

for i in a:
    if i % 2 == 0:
        print(i,"は偶数です")
        continue
    print(i,"奇数です")

# 2-2

n = 3
three = 1
four = 1
for i in range(n):
    three *= 3
    four *= 4
print("3^"+str(n) +" = " ,three)
print("4^"+str(n)  +" = " ,four)
print("3^"+str(n) + "-" + "4^"+str(n)  + " = " ,four - three)