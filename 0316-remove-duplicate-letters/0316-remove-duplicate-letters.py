class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letterCount = Counter(s)
        
        nonDuplicates = []
        seen = set()
        
        for i,letter in enumerate(s):
            if letter in seen:
                letterCount[letter] -= 1
                continue
            while nonDuplicates and letterCount[nonDuplicates[-1]] > 1 and letter <= nonDuplicates[-1]:
                toBeRemoved = nonDuplicates.pop()
                seen.remove(toBeRemoved)
                
                letterCount[toBeRemoved] -= 1
    
            
            nonDuplicates.append(letter)
            seen.add(letter)

        return "".join(nonDuplicates)
                