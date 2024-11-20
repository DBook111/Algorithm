from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        if not prerequisites:
            return True
        set_l = set()
        set_r = set()
        for pair in prerequisites:
            # pre = pair[1] # 先修课            
            # after = pair[0] # 后修课
            set_l.add(pair[0])
            set_r.add(pair[1])
        if len(set_l) != (numCourses - 1):
            return False
        if len(set_r) != (numCourses - 1):
            return False
        
        for i in range(numCourses):
            if i not in set_l:
                index = i
        
        if index in set_r:
            return True
        else:
            return False

class Solution:
    """方法一：有向无环图
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:  
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]: 
                    queue.append(cur)
        return not numCourses

class Solution:
    """方法二：深度优先遍历判断是否有环
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:  
        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            flags[i] = -1
            return True
        
        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True
                    
                

if __name__ == '__main__':
    solu = Solution()
    print(solu.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
            
            