class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num = dict()

        for i in range(len(nums)):
            if nums[i] in dict_num:
                return [i, dict_num[nums[i]]]
            else:
                dict_num[target-nums[i]] = i
