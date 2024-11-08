from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
        """
        stack = []
        if len(pushed) != len(popped):
            return False
        
        # stack.append(pushed[0])
        i, j = 0, 0
        while i < len(pushed):
            if pushed[i] != popped[j]:
                if stack and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    stack.append(pushed[i])
                    i += 1
            else:
                # push and pop
                stack.append(pushed[i])
                i += 1
                stack.pop()
                j += 1
        
        while stack and j < len(popped):
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                break
                
        if not stack:
            return True
        else:
            return False

solu = Solution()
print(solu.validateStackSequences([1,2,3,0], [2,1,3,0]))    