n = int(input())
nums = list(map(int,input().split()))

nums.sort()

if nums[-2]+nums[-3] <= nums[-1]:
    print("NO")
else:
    print("YES")
    nums[-1] , nums[-2] = nums[-2] , nums[-1]
    print(*nums)