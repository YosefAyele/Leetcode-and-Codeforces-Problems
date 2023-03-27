class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        res = 0
        def solve(arr,left,right):
            nonlocal res
            if right - left == 0:
                return [arr[left]]
            
            mid = left + (right - left)//2
            
            l_half = solve(arr,left,mid)
            r_half = solve(arr,mid+1,right)
            
            p1 = 0
            p2 = 0
            
            # first calculate
            while p1 < len(l_half) and p2 < len(r_half):
                
                if l_half[p1] - r_half[p2] <= diff:
                    res += (len(r_half) - p2)
                    p1 += 1
                else:
                    p2 += 1
            
            
            p1 = 0
            p2 = 0
            merged = []
            # now merge
            while p1 < len(l_half) and p2 < len(r_half):
                
                if l_half[p1] <= r_half[p2]:
                    merged.append(l_half[p1])
                    p1 += 1
                else:
                    merged.append(r_half[p2])
                    p2 += 1
            merged.extend(l_half[p1:])
            merged.extend(r_half[p2:])
                    
            return merged
                    
        diff_arr = [nums1[i]-nums2[i] for i in range(len(nums1))]
        
        solve(diff_arr,0,len(nums1)-1)
        
        return res