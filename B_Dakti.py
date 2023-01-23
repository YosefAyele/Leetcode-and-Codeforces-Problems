n=int(input())
for _ in range(n):
    words=input().split()
    output=[]

    for word in words:
        for i,char in enumerate(word):
            if char.isnumeric():
                output.append((char,word[:i]+word[i+1:]))
    output.sort()
    new_output=[]

    for num, word in output:
        new_output.append(word)
    
    print(" ".join(new_output))