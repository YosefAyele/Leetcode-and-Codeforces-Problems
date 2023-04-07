class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def minMax(alice,bob,turn):
            if alice >= bob:
                if turn:
                    return piles[bob]
                else:
                    return -piles[alice]
            if turn:
                aliceLeft = piles[alice] + minMax(alice + 1,bob,not turn)
                aliceRight = piles[bob] + minMax(alice,bob - 1, not turn)
                
                return max(aliceLeft, aliceRight)
            else:
                bobsLeft = -piles[alice] + minMax(alice+1,bob,not turn)
                bobsRight = -piles[bob] + minMax(alice,bob - 1,not turn)
                
                return min(bobsLeft,bobsRight)
            
        return minMax(0,len(piles)-1,True) > 0
        
        
        