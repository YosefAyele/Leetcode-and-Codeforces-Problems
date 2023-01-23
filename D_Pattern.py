n=int(input())
pattern1=input()

idx_set={i:{pattern1[i]} for i in range(len(pattern1))}
for _ in range(n-1):
    pattern=input()

    for i in range(len(pattern)):
        idx_set[i].add(pattern[i])
res=[""]*len(pattern1)

for idx in idx_set:
    char=idx_set[idx]
    if len(char)==1:
        if "?" in char:
            res[idx]="x"
        else:
            res[idx]=char.pop()

    elif len(char)==2:
        if "?" in char:
            char.remove("?")
            res[idx]=char.pop()
        else:
            res[idx]="?"
    else:
        res[idx]="?"
         
print("".join(res))

