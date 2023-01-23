t = int(input())

for _ in range(t):
    
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    for i in range(1,n):
        if arr[i]-arr[i-1] > 1:
            print("NO")
            break
    else:
        print("YES")

