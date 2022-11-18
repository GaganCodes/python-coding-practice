# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# Have to use binary search
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = int(left + (right-left)//2)
            if isBadVersion(mid):
                right = mid-1
            else:
                left = mid+1

        return left
