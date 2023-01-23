n=int(input())
contests=list(map(int,input().split()))
maxm=contests[0]
minm=contests[0]

res=0
for i in range(1,n):
    score=contests[i]
    if score>maxm:
        maxm=score
        res+=1
    elif score<minm:
        minm=score
        res+=1

print(res)
