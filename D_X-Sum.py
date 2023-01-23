t=int(input())

for _ in range(t):
    m, n = map(int,input().split())
    matrix=[list(map(int,input().split())) for i in range(m)]
    
    forward_diagonal_sums={}
    backward_diagonal_sums={}

    for row in range(m):
        for col in range(n):
            backward_diagonal_sums[row-col]=backward_diagonal_sums.get(row-col,0)+matrix[row][col]
            forward_diagonal_sums[row+col]=forward_diagonal_sums.get(row+col,0)+matrix[row][col]
    
    # now calculate the max_sum
    max_sum=0
    for row in range(m):
        for col in range(n):
            cur_sum=forward_diagonal_sums[row+col]+backward_diagonal_sums[row-col]-matrix[row][col]
            max_sum=max(cur_sum,max_sum)
    print(max_sum)

 