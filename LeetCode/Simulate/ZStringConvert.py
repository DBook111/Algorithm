class Solution():
    def convert(self, s: str, numRows: int) -> str:
        inter = []
        row = 1
        direction = 0 # 当前更新行的方向，0代表下，1代表上        
        for c in s:
            # 重构原始输入的字符串，使每个字符带上自己所在的行
            temp = (row, c)
            inter.append(temp)
            if direction == 0:
                row += 1
            else:
                row -= 1
            if row == numRows:
                direction = 1
            if row == 1:
                direction = 0
        # 对重构后的新列表进行排序
        sorted_inter = sorted(inter, key=lambda x: x[0])      
        res = ""
        for i in range(len(s)):
            res += sorted_inter[i][1]
        return res

solu = Solution()
print(solu.convert("abcdefghi", 4))