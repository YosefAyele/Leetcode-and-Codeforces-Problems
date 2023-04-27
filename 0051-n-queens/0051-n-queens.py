class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        n_permutations = list(permutations(range(n)))
        
        res = []
        for position in n_permutations:
            
            checked1 = defaultdict(int)
            checked2 = defaultdict(int)
            
            for i,col in enumerate(position):
                checked1[i - col] += 1
                checked2[i + col] += 1
                
                if checked1[i-col] > 1 or checked2[i + col] > 1:
                    break
            else:
                curr =  [['.']*n for _ in range(n)]
                for row,col in enumerate(position):
                    curr[row][col] = "Q"
                    curr[row] = "".join(curr[row])
                res.append(curr)

        return res
                
                
                
        
        