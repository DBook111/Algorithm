class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i, j = 0, 0
        # for j in range(len(t)):
        #     for i in range(len(s)):
        index = 0
        for i in range(len(s)):
            cur = s[i]
            flag = 0
            # if index > len(t) - 1:
            #     return False
            for j in range(index, len(t)):
                if t[j] == cur:
                    flag = 1
                    index = j + 1
                    break
                else:
                    continue
            if flag == 0:
                return False
        return True

solu = Solution()
print(solu.isSubsequence("aaaaaa", "bbaaaa"))