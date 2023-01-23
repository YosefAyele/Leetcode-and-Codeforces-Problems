t=int(input())
for _ in range(t):
    board=[]
    for i in range(8):
       line=input()
       if len(line)==8:
             board.append(list(line))
    directions=[(-1,-1),(-1,1),(1,-1),(1,1)]
    for row in range(1,7):
        for col in range(1,7):
            if board[row][col]=="#":
                isPosition=True
                for dx,dy in directions:
                    cur_row=row+dx
                    cur_col=col+dy
                    if board[cur_row][cur_col]!="#":
                        isPosition=False
                if isPosition:
                    print(row+1,col+1)
                    break