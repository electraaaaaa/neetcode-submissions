class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] = -nums[k]
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue # skip teh duplicate

            left, right = i + 1, len(nums) - 1
            #doing a two sum on the rest of the list
            while left < right:
                threesum = a + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    # threesum == 0
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 #move pointer to skip duplicate on the left. 
        return res