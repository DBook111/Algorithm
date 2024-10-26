class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.index(i) for i in s] == [t.index(j) for j in t]
        # dic = dict()
        # for i, c in enumerate(s):
        #     if c not in dic:
        #         if t[i] in dic:
        #             if dic[t[i]] != c:
        #                 return False   
        #         dic[c] = t[i] 
        #     else:
        #         if dic[c] == t[i]:
        #             continue
        #         else:
        #             return False
        # return True
    
    
so = Solution()
print(so.isIsomorphic("paper", "title")) # 01034 01034