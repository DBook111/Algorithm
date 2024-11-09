from typing import List

class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        k神解法
        """
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i]) # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res

    def spiralOrder_zzl(self, matrix: List[List[int]]) -> List[int]:
        """
        定义 4 个方向
        """
        # 行边界
        height = len(matrix)
        # 列边界
        width = len(matrix[0])
        
        i, j = 0, 0
        # 转向的边界条件
        hashSet = set()
        
        res = []
        while len(res) != (height * width):
            # 如何判断该变向了?  1. i或j撞到边界 2. (i, j)在 hash set 中
            
            # 向右
            while (j < width) and ((i, j) not in hashSet):
                res.append(matrix[i][j])
                hashSet.add((i, j))
                j += 1
            j -= 1
            i += 1   
            # 向下
            while (i < height) and ((i, j) not in hashSet):
                res.append(matrix[i][j])
                hashSet.add((i, j))
                i += 1
            i -= 1
            j -= 1    
            # 向左
            while (j > -1) and ((i, j) not in hashSet):
                res.append(matrix[i][j])
                hashSet.add((i, j))
                j -= 1
            j += 1
            i -= 1    
            # 向上
            while (i > -1) and ((i, j) not in hashSet):
                res.append(matrix[i][j])
                hashSet.add((i, j))
                i -= 1
            i += 1
            j += 1                
        return res

solu = Solution()
print(solu.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))