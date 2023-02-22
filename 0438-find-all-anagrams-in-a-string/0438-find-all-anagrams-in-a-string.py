class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        current = {}
        p_count = Counter(p)
        res = []

        for right,letter in enumerate(s):

            current[letter] = current.get(letter,0) + 1

            if right - left + 1 == len(p):

                if current == p_count:
                    res.append(left)
                current[s[left]] -= 1
                if current[s[left]] == 0:
                    current.pop(s[left])
                left += 1
                
        return res

