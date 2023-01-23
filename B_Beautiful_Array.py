n=int(input())
nums=list(map(int,input().split()))
neg=set()
pos=set()
zer=set()
maxLimit=n//3
pro_pos=1
pro_neg=1
for num in nums:
    if num<0:
        neg.add(num)
    elif num>0:
        pos.add(num)
    else:
        zer.add(num)
if len(pos)==0:
    pos.add(neg.pop())
    pos.add(neg.pop())
if not len(neg)%2:
    zer.add(neg.pop())
print(len(neg),*neg)
print(len(pos),*pos)
print(len(zer),*zer)