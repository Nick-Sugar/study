score = [ 70,98,92,88,64]

total = 0

for i in score:
    total += i

average = total / len(score)

print("合計点",total)
print("平均点",average)