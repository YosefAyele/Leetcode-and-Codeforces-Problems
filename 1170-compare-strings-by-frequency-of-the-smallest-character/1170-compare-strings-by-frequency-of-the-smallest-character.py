class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def freq(string):
            
            smallest = min(string)
            counts= Counter(string)
            
            return counts[smallest]
        
        
        words = [freq(word) for word in words]
        queries = [freq(word) for word in queries]
        
        words.sort()
        
        res = []
        for query in queries:
            
            curr = len(words) - bisect.bisect_right(words,query)
            
            res.append(curr)
        
        return res