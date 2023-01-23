t = int(input())
for _ in range(t):
    n , m = map(int,input().split())
    grid = [list(input()) for _ in range(n)]
    res = 0 
    last_row = n-1
    last_col = m-1

    lastRs =0
    lastDs = 0

    # count Number of Ds on the last row
    for i in range(m):
        if grid[last_row][i] == "D":
            res += 1
    # Count Number of Rs on the last col
    for i in range(n):
        if grid[i][last_col] == "R":
            res += 1
    
    print(res)

