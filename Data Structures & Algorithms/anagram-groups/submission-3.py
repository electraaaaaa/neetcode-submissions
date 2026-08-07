class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # map charcount to list of anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            #loop thru every character in the string
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)
            # grouped the count together

        lst = []

        for value in res.values():
            lst.append(value)
        return lst