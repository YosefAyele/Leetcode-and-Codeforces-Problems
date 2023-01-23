n,k=map(int,input().split())
lectures=list(map(int,input().split()))
state=list(map(int,input().split()))

initial_sum=sum(lectures[i] for i in range(n) if state[i]==1)
res=initial_sum

l=0
for r in range(n):
    if state[r]==0:
        initial_sum+=lectures[r]
    res=max(res,initial_sum)
    if r-l+1==k:
       
        if state[l]==0:
            initial_sum-=lectures[l]
        l+=1
print(res)
    

