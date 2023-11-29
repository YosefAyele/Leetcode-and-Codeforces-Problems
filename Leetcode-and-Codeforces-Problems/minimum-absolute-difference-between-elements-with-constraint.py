class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        from sortedcontainers import SortedList

        sorted_list = SortedList()
        ans = inf
        n = len(nums)

        for i in range(n-x-1,-1,-1):
            sorted_list.add(nums[i+x])

            idx = bisect.bisect_left(sorted_list,nums[i])

            if idx < len(sorted_list):
                ans = min(ans,abs(sorted_list[idx] - nums[i]))
            if idx > 0:
                ans = min(ans,abs(sorted_list[idx-1] - nums[i]))

        return ans