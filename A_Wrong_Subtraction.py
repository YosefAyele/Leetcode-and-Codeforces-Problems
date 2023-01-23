number , k = map(int,input().split())
for _ in range(k):
    if number%10:
        number-=1
    else:
        number//=10
print(number)