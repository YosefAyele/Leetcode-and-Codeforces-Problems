n = int(input())
res = 0 
for _ in range(n):
    execute = set(input())

    if "+" in execute:
        res+=1
    else:
        res-=1
    
print(res)
    

