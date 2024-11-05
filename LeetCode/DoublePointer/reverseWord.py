class Solution:
    def reverseWords(self, s: str) -> str:
        # 定义两个左右指针
        l, r = 0, 0
        # 定义一个栈
        stack = []
        while r < len(s):
            # 如果 s[r] 不是英文字符，将r右滑
            if s[r] == ' ':
                r += 1
                continue
            # 更新 l 的位置
            l = r
            # 此时的 s[r] 是英文字符，将其移动到单词的最右边
            while (r+1 < len(s)) and (s[r+1] != ' '):                
                r += 1
            # 此时，l在单词的左边，r在单词的右边，逆序进栈
            for i in range(r, l-1, -1):
                stack.append(s[i])
            # 单词全部入栈后，追加一个空格
            stack.append(' ')
            # 该单词入栈后，r移动到右边
            r += 1
        # 出栈，生成最终结果
        res = ''
        # 先排一个没用的空格
        stack.pop()
        while stack:
            zzl = stack.pop()
            res += zzl  
        return res      
                
    
solu = Solution()
zzl = solu.reverseWords("a good   example")
print(zzl)