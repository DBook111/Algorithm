from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)   
        last_temp = None 
        for i in range(l):
            if last_temp == numbers[i]:
                continue
            last_temp = numbers[i]
            j = i + 1
            for j in range(j, l):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        return None        
    
    
sol = Solution()
res = sol.twoSum([2,7,11,15], 9)
print(res)