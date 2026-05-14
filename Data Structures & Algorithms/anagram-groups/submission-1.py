class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)

        for s in strs:
            count = [0] * 26 # for the number of letters in the alphabet

            for character in s:
                index = ord(character) - ord("a")
                count[index] += 1 # increment the character at index by 1
            
            collection[tuple(count)].append(s)
        lst = []

        for val in collection.values():
            lst.append(val)
        return lst
