from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l-1, -1, -1):
            if nums[i-1] is not None and nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]
        
solu = Solution()
print(solu.findMin([1,3,5]))