def addup(N):
    count = 0
    for i in range(1,N + 1):
        count += i
    return count

print(addup(10))