class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        n_permutations = list(permutations(range(n)))
        
        res = []
        for position in n_permutations:
            
            checkd1 = set()
            checkd2 = set()
            
            for i,col in enumerate(position):
                checkd1.add(i-col)
                checkd2.add(i+col)
            if len(checkd1) == len(checkd2) == n:
                curr =  [['.']*n for _ in range(n)]
                for row,col in enumerate(position):
                    curr[row][col] = "Q"
                    curr[row] = "".join(curr[row])
                res.append(curr)
        
        return res
                
                
                
        
        