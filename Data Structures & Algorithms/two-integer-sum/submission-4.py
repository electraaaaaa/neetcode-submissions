class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for index, number in enumerate(nums):
            subtract = target - number
            if subtract in prevMap:
                return [prevMap[subtract], index]
            prevMap[number] = index