class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        charMod = {(97 + i)%26:chr(97+i) for i in range(26)}
        # print(charMod)
        
        shiftTable = [0]*(len(s) + 1)
        
        for start,end,direction in shifts:
            
            if direction == 1:
                shiftTable[start] += 1
                shiftTable[end+1] -= 1
            else:
                shiftTable[start] -= 1
                shiftTable[end+1] += 1
        
        finalShifts = list(accumulate(shiftTable))
        
        res = []
        
        for i,letter in enumerate(s):
            
            currMod = (ord(letter) + finalShifts[i]) % 26
            
            res.append(charMod[currMod])
        
        return ''.join(res)
    
    
    
    
            