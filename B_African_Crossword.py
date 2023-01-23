m, n = map(int,input().split())

table= [ list(input()) for _ in range(m)]

# print(table)

for row in range(m):
    for col in range(n):
        letter = table[row][col]
        # check throughout the row
        flag=False
        if letter != ".":

            for k in range(n):
                if k!=col and  table[row][k] == letter:
                    flag = True
                    table[row][k] = "."

            # check throughout the column
            for k in range(m):
                if k!=row and  table[k][col] == letter:
                    flag = True
                    table[k][col] = "."
            if flag:
                table[row][col] = "."
res = ""

print(table)
for row in range(m):
    for col in range(n):
        curr_letter = table[row][col]

        if curr_letter != ".":
            res+=curr_letter

print(res)



