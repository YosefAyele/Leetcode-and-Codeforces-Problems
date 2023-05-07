class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        heapq.heapify(heap)
        
        res = []
        heapq.heappush(heap,(nums1[0] + nums2[0], 0,0))
        visited = set()
        while heap and len(res) < k:
            _,i,j = heapq.heappop(heap)
            
            if (i,j) not in visited:
                res.append([nums1[i],nums2[j]])
                visited.add((i,j))
                
                i_ = i + 1
                j_ = j + 1
                
                if i_ < len(nums1):
                    heapq.heappush(heap,(nums1[i_] + nums2[j],i_,j))
                if j_ < len(nums2):
                    heapq.heappush(heap,(nums1[i] + nums2[j_],i,j_))
        return res
                