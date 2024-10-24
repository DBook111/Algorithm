# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         self.s = s
#         self.t = t
#         zzl = []
#         for c in self.s:
#             zzl.append(c)
#         for c in self.t:
#             if c in zzl:
#                 zzl.remove(c)
#         if len(zzl) == 0:
#             return True
#         else:
#             return False

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        zzl = defaultdict(int)
        for c in s:
            zzl[c] += 1
        for c in t:
            zzl[c] -= 1
        for val in zzl.values():
            if val != 0:
                return False
        return True        

solu = Solution()
print(solu.isAnagram("aacc", "ccac"))