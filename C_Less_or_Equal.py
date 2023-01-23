n , k = map(int,input().split())
nums=list(map(int,input().split()))

nums.sort()

if k==0:
    ans=nums[0]-1 if nums[0]-1>0 else -1
    print(ans)
else:
    ans=nums[k-1]
    cnt=0
    for num in nums:
        if num<=ans:
            cnt+=1
    if cnt!=k or ans<1:
        print(-1)
    else:
        print(ans)