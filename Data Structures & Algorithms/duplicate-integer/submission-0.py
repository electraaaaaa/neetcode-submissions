class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collected = {}
        for val in nums:
            if val not in collected:
                collected[val] = 1
            else:
                collected[val] += 1
            if collected[val] == 2:
                return True
        return False