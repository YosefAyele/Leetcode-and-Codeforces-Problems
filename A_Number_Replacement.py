t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    string=input()

    arr_string={}

    for i in range(n):
        if arr[i] in arr_string:
            if arr_string[arr[i]]!=string[i]:
                print("NO")
                break
        else:
            arr_string[arr[i]]=string[i]
    else:
        print("YES")

