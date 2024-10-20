class Solution:    
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)
        if length > 10**4:
            return False
        keys = {"{": "}", 
                "(": ")",
                "[": "]"
                }
        for i in range(length):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                current = stack.pop()
                if keys[current] == s[i]:
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        return True

if __name__ == "__main__":
    solu = Solution()
    bool = solu.isValid(")")
    print(bool)