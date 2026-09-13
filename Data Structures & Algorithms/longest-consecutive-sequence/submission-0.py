class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for number in numsSet:
            if number - 1 not in numsSet:
                length = 1
                while number + length in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest