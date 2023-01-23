n=int(input())
ints=list(map(int,input().split()))

# first find the last number of the sequence
numbers=set(ints)
for num in ints:
  
    if num%3 and num*2 not in numbers:
        last=num
        break
    elif num//3 not in numbers and num*2 not in numbers:
        last=num
        break
added=set()

res=[]
for _ in range(n):
    res.append(last)
    added.add(last)

    if last//2 in numbers and last//2 not in added:
        last//=2
    elif last*3 in numbers and last*3 not in added:
        last*=3
print(*reversed(res))
    

    






    
