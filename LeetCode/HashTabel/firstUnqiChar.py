# 给定一个字符串 s ，找到他的第一个不重复的字符， 并返回他的索引。如果不存在，则返回-1

class Meter():
    def __init__(self):
        self.index: list = []
        # self.data: str = None
        self.time: int = 0
    
    def add(self, index):
        self.time += 1
        # self.data = data
        self.index.append(index)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, c in enumerate(s):
            if c in dic:
                dic[c].add(i)
                continue
            me = Meter()
            me.add(i)
            dic[c] = me
        for key in dic.keys():
            if dic[key].time == 1:
                return dic[key].index[0]
        return -1

if __name__ == '__main__':
    solu = Solution()
    print(solu.firstUniqChar("aabb"))
            