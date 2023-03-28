class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        res = [0]*len(nums)
        def solve(arr,left,right):
            
            if right - left == 0:
                return [arr[left]]
            
            mid = left + (right - left) // 2
            
            l = solve(arr,left,mid)
            r = solve(arr,mid+1,right)
            
            
            
            merged = []
            p1 = 0
            p2 = 0
            
            while p1 < len(l) and p2 < len(r):
                
                if l[p1][0] > r[p2][0]:
                    # res[l[p1][1]] += 1
                    merged.append(r[p2])
                    p2 += 1

                else:
                    res[l[p1][1]] += p2
                    merged.append(l[p1])
                    p1 += 1
                    
            merged.extend(l[p1:])
            merged.extend(r[p2:])
            
            while p1 < len(l):
                res[l[p1][1]] += p2
                p1 += 1

           
            
                
            return merged
        
        arr = [(nums[i],i) for i in range(len(nums))]
        # print(arr)
        
        solve(arr,0,len(nums)-1)
        
        return res

                    