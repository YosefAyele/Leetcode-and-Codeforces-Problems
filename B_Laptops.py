n = int(input())
price_quality = []
for _ in range(n):
    a , b = map(int,input().split())
    price_quality.append((a,b))
price_quality.sort()
for i in range(1,n):
    if price_quality[i][1] < price_quality[i-1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")