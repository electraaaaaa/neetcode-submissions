class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = {}
        for string in strs:
            # check if it's inside the collection
            stri = ''.join(sorted(string))
            if stri in collection:
                collection[stri] += [string]
            else:
                collection[stri] = [string]

        lst = []
        for vals in collection.values():
            lst.append(vals)
        return lst
            


    
# def is_anagram(string: str, string2: str) -> bool:
#     count1 = {}
#     count2 = {}
#     if len(string) != len(string2):
#         return False

#     for i in range(len(string)):
#         count1[string[i]] = 1 + count1.get(string[i])
#         count2[string2[i]] = 1 + count2.get(string2[i])
    
#     for c in count1:
#         if count1[c] != count2[c]:
#             return False
#     return True
