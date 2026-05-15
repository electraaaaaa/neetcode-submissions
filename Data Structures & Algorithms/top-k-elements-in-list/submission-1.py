class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collection = {}

        for number in nums:
            collection[number] = 1 + collection.get(number, 0)
        
        lst = []
        for key, val in collection.items():
            lst.append((key, val))
            lst.sort(key=lambda x: x[1], reverse=True)
            if len(lst) > k:
                lst.pop()

        return [tup[0] for tup in lst]