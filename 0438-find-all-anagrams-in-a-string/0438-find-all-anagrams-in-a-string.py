class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        
        p_count = Counter(p)
        res = []

        for right,letter in enumerate(s):
            if letter in p_count:
                p_count[letter] -= 1
            
            if right - left + 1 == len(p):
                check = True
                for letter in p_count:
                    if p_count[letter] != 0:
                        check = False
                if check:
                    res.append(left)
                if s[left] in p_count:
                    p_count[s[left]] += 1
                left += 1

        return res

