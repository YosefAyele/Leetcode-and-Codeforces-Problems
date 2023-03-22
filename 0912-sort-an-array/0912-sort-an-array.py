class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)

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
        
        return mergeSort(0,len(nums)-1,nums)