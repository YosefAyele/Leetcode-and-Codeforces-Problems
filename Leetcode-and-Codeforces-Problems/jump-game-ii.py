class Solution:
    def jump(self, nums: List[int]) -> int:
        
        max_after_jump_positions = []

        max_ = 0
        for i,step in enumerate(nums):
            max_ = max(max_,step+i)
            max_after_jump_positions.append(max_)

        idx = 0
        ans = 0
        while idx < len(nums) - 1:
            idx = max_after_jump_positions[idx]
            ans += 1

        return ans
