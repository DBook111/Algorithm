from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 高
        height = len(matrix)
        # 宽
        width = len(matrix[0])
        # hash
        hashSet = set()
        # 转置
        for i in range(height):
            for j in range(width):
                if i == j:
                    continue
                if (i, j) in hashSet:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                hashSet.add((j, i))
        # 对每一行进行逆序
        for i in range(height):
            matrix[i].reverse()

# solu = Solution()
# zzl = [[1,2,3],[4,5,6],[7,8,9]]
# solu.rotate(zzl)
# print(zzl)