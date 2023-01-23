t = int(input())
for _ in range(t):
    n , k = map(int,input().split())
    arr = list(map(int,input().split()))
    res = 0 
    l = 0

    for r,num in enumerate(arr):

        if r and num*2 <= arr[r-1]:
            l = r
        if r-l == k:
            if l<n-k:
                res+=1
            l+=1 
            
    print(res)
        