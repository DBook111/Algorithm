from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 先对列表求和，然后从左向右遍历
        total = sum(nums)
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if (total - current_sum) == (current_sum - nums[i]):
                return i
        return -1

solu = Solution()
print(solu.pivotIndex([2, 1, -1]))