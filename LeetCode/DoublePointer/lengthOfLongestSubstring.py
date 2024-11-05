

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1        
        hash = {}
        current_count = 0
        max_substring = 0
        i = 0
        switch = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in hash.values():
                    current_count += 1
                    hash[j] = s[j]
                else:
                    switch = 1
                    if current_count > max_substring:
                        max_substring = current_count
                    current_count = 0
                    hash = {}
                    break
        if switch == 1 and max_substring == 0:
            return current_count
        return max_substring
                
                                                        

solu = Solution()
print(solu.lengthOfLongestSubstring("qrsvbspk"))                  