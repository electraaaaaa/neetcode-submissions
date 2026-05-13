class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        # add each element to the dictionary with the key being the string
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # check each element in the hashmap and check if any are different.
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True 