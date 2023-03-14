class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights = [0] + heights + [0]
        nextLess = [-1]*len(heights)
        mon = []
        for i,num in enumerate(heights):
            while mon and num < heights[mon[-1]]:
                
                nextLess[mon.pop()] = i
                
            mon.append(i)
        
        prevLess = [-1]*len(heights)
        mon = []
        for i in range(len(heights)-1,-1,-1):
            num = heights[i]
            while mon and num < heights[mon[-1]]:
                
                prevLess[mon.pop()] = i
                
            mon.append(i)
        
        
        ans = 0
        
        for i in range(1,len(heights) - 1):
            num = heights[i]
            
            curr = num * (nextLess[i] - prevLess[i] - 1)
            ans = max(ans,curr)
        
        return ans
            