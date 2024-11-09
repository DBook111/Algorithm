from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        nums = list(range(1, n ** 2 + 1))
        i, j = 0, 0
        hash_set = set()
        count = 0
        while count != (n ** 2):
            # 向右
            while (j < n) and ((i, j) not in hash_set):
                matrix[i][j] = nums[count]
                count += 1
                hash_set.add((i, j))
                j += 1
            j -= 1
            i += 1
            # 向下
            while (i < n) and ((i, j) not in hash_set):
                matrix[i][j] = nums[count]
                count += 1
                hash_set.add((i, j))
                i += 1
            i -= 1
            j -= 1    
            # 向左
            while (j > -1) and ((i, j) not in hash_set):
                matrix[i][j] = nums[count]
                count += 1
                hash_set.add((i, j))
                j -= 1
            j += 1
            i -= 1    
            # 向上
            while (i > -1) and ((i, j) not in hash_set):
                matrix[i][j] = nums[count]
                count += 1
                hash_set.add((i, j))
                i -= 1
            i += 1
            j += 1
        return matrix

solu = Solution()
print(solu.generateMatrix(3))
        