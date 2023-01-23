t = int(input())

for _ in range(t):
    n , m = map(int,input().split())
    res = (n*m)//2+1 if (n*m)%2 else (n*m)//2
    print(res)