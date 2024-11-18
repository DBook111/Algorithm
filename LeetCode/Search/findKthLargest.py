from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # i = 0
        # for i in range(k):
        #     for j in range(len(nums)-1-i):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        # return nums[len(nums)-k]
        return sorted(nums)[len(nums)-k]