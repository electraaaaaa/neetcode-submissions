class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_total = 1
        count_of_zeroes = 0
        product_total_for_zeroes = 1
        for num in nums:
            # so regular product total
            product_total *= num
            if num != 0:
                # if the number isn't zero, then increase product total for zero entries
                product_total_for_zeroes *= num
            if num == 0:
                # if number is 0, increase the count by 1. 
                count_of_zeroes += 1
        
        res = []
        for num in nums:
            if num == 0:
                if count_of_zeroes == 1:
                    res.append(product_total_for_zeroes)
                else:
                    # otherwise, 0 appeared more than once. 
                    res.append(0)
            else:
                # num is not 0
                res.append(int(product_total / num))

        return res