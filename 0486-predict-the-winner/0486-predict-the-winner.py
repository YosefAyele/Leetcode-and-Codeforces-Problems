class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        
        def score(left,right,turn):
            
            if left >= right:
                if turn:
                    return nums[left]
                else:
                    return -nums[right]
            
            if turn:
                
                leftSide = nums[left] + score(left+1,right,not turn)
                rightSide = nums[right] + score(left,right-1,not turn)
                
                return max(leftSide,rightSide)
            
            else:
                
                leftSide = -nums[left] + score(left+1,right,not turn)
                rightSide = -nums[right] + score(left,right-1,not turn)
                
                return min(leftSide,rightSide)
        
        return score(0,len(nums)-1,True) >= 0
                
            