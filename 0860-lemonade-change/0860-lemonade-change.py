class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        fives = 0
        tens = 0
        
        
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives < 1:
                    return False
                fives -= 1
                tens += 1
            else:
                if not tens:
                    if fives < 3:
                        return False
                    fives -= 3
                else:
                    if fives < 1:
                        return False
                    tens -= 1
                    fives -= 1
        return True
                    
        