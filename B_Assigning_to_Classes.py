t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    a.sort()
    median = n

    print(a[median]-a[median-1])