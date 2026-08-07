class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}

        for number in nums:
            if number in res.keys():
                res[number] += 1
            else:
                res[number] = 1
        # now we have a dictionary that maps the number to the number of times it appears. 

        sorted_lst = sorted(res.items(), key=lambda item: item[1])

        # now we have a sorted list of tuples

        lst = []
        for i in range(k):
            lst.append(sorted_lst[len(sorted_lst)-1-i][0])

        return lst
        # now we have a list of tuples ig. 