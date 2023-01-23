n=int(input())
string=input()

freq={}
l=0
for r in range(1,n):
       
    freq[string[l:r+1]]=freq.get(string[l:r+1],0)+1
    l+=1

res=''
max_freq=0
for twoGram in freq:
    if freq[twoGram]>max_freq:
        res=twoGram
        max_freq=freq[twoGram]
print(res)