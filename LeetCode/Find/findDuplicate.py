from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):            
            if (nums[i+1] is not None) and (nums[i] == nums[i + 1]):
                return nums[i]        


solu = Solution()
print(solu.findDuplicate([3,1,3,4,2]))