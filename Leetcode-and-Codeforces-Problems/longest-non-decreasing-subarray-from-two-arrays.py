class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        prevMin,prevMax = 0,0
        prevMinDist,prevMaxDist = 0,0
        ans = 0

        for i in range(len(nums1)):
            currMinDist,currMaxDist = 1,1

            currMin,currMax = min(nums1[i],nums2[i]), max(nums1[i],nums2[i])

            if currMin >= prevMin:
                currMinDist = prevMinDist + 1
            if currMin >= prevMax:
                currMinDist = max(currMinDist,prevMaxDist+1)
            
            if currMax >= prevMin:
                currMaxDist = prevMinDist + 1
            if currMax >= prevMax:
                currMaxDist = max(currMaxDist,prevMaxDist + 1)
            
            prevMin,prevMax = currMin, currMax
            prevMinDist,prevMaxDist = currMinDist, currMaxDist

            ans = max(ans,currMinDist,currMaxDist)
        
        return ans

            
