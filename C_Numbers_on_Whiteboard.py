t = int(input())

for _ in range(t):
    n = int(input())
    print(2)
    curr = n
   
    while n>1:
         print(curr , n-1)
         curr = (curr + n -1)//2 + 1 if (curr + n -1)%2 else (curr + n -1)//2
         n -= 1


            