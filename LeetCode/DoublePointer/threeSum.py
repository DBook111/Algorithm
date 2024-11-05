from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 先排序
        res = []
        l = len(nums)
        
        for i in range(l):
            # 避免重复计算相同的第一个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 使用双指针方法查找剩余的两个数
            left, right = i + 1, l - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过重复的nums[j]
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        
                    # 跳过重复的nums[k]
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 移动指针继续寻找
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1
                    
                else:
                    right -= 1
        
        return res
