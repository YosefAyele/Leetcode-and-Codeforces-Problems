class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        ans = 0
        def divide(left,right,arr):
            nonlocal ans
            if right - left == 0:
                return [arr[left]]
            
            mid = left + (right - left) // 2
            left_half = divide(left,mid,arr)
            right_half = divide(mid+1,right,arr)
            # first count the number of pairs that satisfy the conditions
            p1 = 0
            p2 = 0
            
            while p1 < len(left_half) and p2 < len(right_half):
                while p2<len(right_half) and left_half[p1] > 2*right_half[p2]:
                    p2 += 1
                ans += p2
                p1 += 1
            
            while p1 < len(left_half):
                ans += p2
                p1 += 1
            
            # now merge the two sorted arrays
            l_half = 0
            r_half = 0
            merged = []

            while l_half < len(left_half) and r_half < len(right_half):
                if left_half[l_half] <= right_half[r_half]:
                    merged.append(left_half[l_half])
                    l_half += 1

                else:
                    merged.append(right_half[r_half])
                    r_half += 1
            merged.extend(left_half[l_half:])
            merged.extend(right_half[r_half:])

            return merged

        divide(0,len(nums)-1,nums)
        
        return ans
            
            
            