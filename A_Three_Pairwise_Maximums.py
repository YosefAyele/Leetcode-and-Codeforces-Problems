from collections import Counter
t = int(input())

for _ in range(t):
    a = list(map(int,input().split()))
    counts = Counter(a)

    max_ = max(a)
    min_ = min(a)

    if len(counts) == 1:
        print("YES")
        print(max_,max_,max_)
    elif len(counts) == 2:
        if counts[max_] == 2:
            print("YES")
            print(max_ , min_ , min_)
        else:
            print("NO")
    else:
        print("NO")
