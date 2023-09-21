N, M = map(int, input().split())
coin = [int(input()) for i in range(int(N))]

total = 0

while True:
    if M == 0:
        print(total)
        break

    for c in range(len(coin)):
        if coin[c] <= M and c == N-1:
            num = M // coin[c]
            M -= num * coin[c]
            total += num
            continue        

        if coin[c] > M:
            num = M // coin[c-1]
            M -= num * coin[c-1]
            total += num
            continue




    

