# Hashset solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False

# Dictionary solution (Hash map)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = dict()

        for num in nums:
            if num in numDict:
                return True
            else:
                numDict[num]=1
