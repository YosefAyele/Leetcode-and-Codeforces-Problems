t=int(input())
for _ in range(t):
    n=int(input())

    grid=[list(input()) for _ in range(n)]
  

    res=0
    seen=set()
    for row in range(n):
        for col in range(n):
            current_position = grid[row][col]
            rotated90 = grid[n-col-1][row]
            rotated180 = grid[n-row-1][n-col-1]
            rotated270 = grid[col][n-row-1]
            
            if (row,col) not in seen:
                ones=int(current_position)+int(rotated180)+int(rotated270)+int(rotated90)
                res+=min(ones,4-ones)
                
                seen.add((row,col))
                seen.add((n-1-col,row))
                seen.add((n-row-1,n-col-1))
                seen.add((col,n-row-1))
    print(res)  


