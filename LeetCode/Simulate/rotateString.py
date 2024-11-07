from collections import deque

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        s
        """
        if len(s) != len(goal):
            return False
        queue = deque()
        rotate = False
        # 扫描 s ，如果和goal的第一个匹配上了，就开始
        for i in range(len(s)):
            if s[i] == goal[0]:
                # 如果匹配上了，再进一步看后续是否匹配
                j = i + 1
                for k in range(j, len(s)):
                    if s[k] == goal[k-len(queue)]:
                        rotate = True
                    else:
                        # 如果不匹配，将该字符加入队列
                        queue.append(s[i])
                        rotate = False
                        break
                if rotate == True or (i + 1 == len(s)):
                    # 如果第一轮考验没问题，再经历第二轮考验                    
                    for w in range(len(queue)):
                        if queue[w] == goal[len(goal) - len(queue) + w]:
                            rotate = True
                        else: 
                            rotate = False
                            break
                    # check 是否通过第二轮的考验
                    if rotate == True:
                        # 通过
                        return True
                    else:
                        # Fail
                        return False
            else:
                # 没匹配上，就放入队列
                queue.append(s[i])
        # 跑了一轮都没匹配上
        return False

solu = Solution()
print(solu.rotateString("bbbacddceeb", "ceebbbbacdd"))