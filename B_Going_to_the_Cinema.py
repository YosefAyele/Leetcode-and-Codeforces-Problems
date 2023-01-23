t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    a.sort()
    # print(a)
    res = 0
    for i in range(n-1,-1,-1):
        notGoing = a[i+1] if i+1<n else float('inf')
        going = i

        if notGoing > i+1 and going >= a[i]:
            res+=1
    print(res + int(a[0] != 0))
