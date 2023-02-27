class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_len = max(max_len,len(window))
        
        return max_len