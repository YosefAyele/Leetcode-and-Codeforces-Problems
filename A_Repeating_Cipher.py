n = int(input())
cipher = input()

res = []
i=0
repetition = 0
while i<n:
    res.append(cipher[i])
    repetition+=1
    i+=repetition
print("".join(res))