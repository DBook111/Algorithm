# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j = 0, n-1
        mid = (i + j) // 2
        while i <= j:
            if isBadVersion(mid) == False:
                i = mid + 1
                mid = (i + j) // 2
            else:
                j = mid - 1
                mid = (i + j) // 2
        return i  