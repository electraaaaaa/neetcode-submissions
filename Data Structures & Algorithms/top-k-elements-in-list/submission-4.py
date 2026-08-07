class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq =  [[] for _ in range(len(nums) + 1)]

        for number in nums:
            count[number] = 1 + count.get(number, 0)

        for number, count in count.items():
            freq[count].append(number)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for number in freq[i]:
                res.append(number)
                if len(res) == k:
                    return res