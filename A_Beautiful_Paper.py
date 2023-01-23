t=int(input())
for _ in range(t):
    a1,b1 = map(int,input().split())
    a2,b2 = map(int,input().split())
    if max(a1,b1)!=max(a2,b2):
        print("No")
    else:
        if min(a1,b1)+min(a2,b2)==max(a1,b1):
            print("Yes")
        else:
            print("No")