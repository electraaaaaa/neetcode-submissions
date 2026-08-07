class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in hashmap.keys():
                hashmap[sorted_string].append(string)
            else:
                hashmap[sorted_string] = [string]
        
        lst = []
        for key, value in hashmap.items():
            lst.append(value)
        return lst

